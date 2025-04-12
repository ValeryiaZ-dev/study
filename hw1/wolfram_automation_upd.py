"""
решение с использованием библиотеки mpi.
"""

from mpi4py import MPI
import numpy as np
import sys
import time

# Length of the string
N = 100  # 40000000

# Number of iterations
Nit = 100  # 10

def main(r):
    comm = MPI.COMM_WORLD
    prank = comm.Get_rank()
    psize = comm.Get_size()

    if len(sys.argv) < 3:
        if prank == 0:
            print("Usage: mpirun -np <num_processes> python3 cellular_automaton.py <rule> <output_file>")
        sys.exit(1)

    rule = [0, 1, 0, 0, 1, 0, 1, 1]
    r1 = r
    for i in range(7, -1, -1):
        rule[i] = r1 // (1 << i)
        r1 -= (r1 // (1 << i)) * (1 << i)

    sizeRank = N // psize + (1 if (prank + 1) <= (N % psize) else 0)
    offset = sizeRank * prank
    sizeRow = sizeRank + 2
    charSize = sizeRank + (1 if prank == (psize - 1) else 0)

    buf = np.zeros(charSize, dtype='int8')
    if prank == (psize - 1):
        buf[-1] = ord('\n')
    row = np.random.randint(2, size=sizeRow, dtype='int8')
    rowChanged = np.zeros(sizeRow, dtype='int8')

    # на некоторых операционных системах time() возращает cpu time, то есть время будет умножаться на кол-во использованных ядер
    # но на моем ноутбуке все было ок, но еще есть MPI.Wtime(), который точно возвращает wall time вне зависимости от ОС
    t1 = time.time()

    #открываем файл через мпишный file handle
    fh = MPI.File.Open(comm, sys.argv[2], MPI.MODE_CREATE | MPI.MODE_WRONLY)

    for j in range(Nit):
        if psize > 1:
            # можно убрать if'ы если с % вычислять dest
            comm.Isend(row[1:2], dest=(prank-1+psize)%psize, tag=1)
            comm.Isend(row[-2:-1], dest=(prank+1)%psize, tag=0)
            #if prank == 0:
            #    comm.Isend(row[1:2], dest=psize-1, tag=1)
            #    comm.Isend(row[-2:-1], dest=1, tag=0)
            #elif prank == psize - 1:
            #    comm.Isend(row[1:2], dest=psize-2, tag=1)
            #    comm.Isend(row[-2:-1], dest=0, tag=0)
            #else:
            #    comm.Isend(row[1:2], dest=prank-1, tag=1)
            #    comm.Isend(row[-2:-1], dest=prank+1, tag=0)

            comm.Recv(row[0:1], source=MPI.ANY_SOURCE, tag=0)
            comm.Recv(row[-1:], source=MPI.ANY_SOURCE, tag=1)

            comm.Barrier()
        else:
            row[0] = row[-2]
            row[-1] = row[1]

        for i in range(1, sizeRow - 1):
            rowChanged[i] = rule[4 * row[i-1] + 2 * row[i] + row[i+1]]

        row[1:-1] = rowChanged[1:-1]
        buf[:sizeRank] = rowChanged[1:-1] + ord('0')

        # пишем в файлик
        fh.Write_at_all(offset, buf)
        offset += N + 1

        comm.Barrier()

    # закрываем file handle
    fh.Close()

    t2 = time.time()
    if prank == 0:
        print(f"MPI_Wtime: {t2 - t1:.4f}")

if __name__ == "__main__":
    main(r=int(sys.argv[1]))

