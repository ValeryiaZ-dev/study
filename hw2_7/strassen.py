"""
Формулировка задания: необходимо реализовать метод Штрассена перемножения квадратных матриц
"""

matrix_a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix_b = [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]


def strassen(matrix_a, matrix_b):
    n = len(matrix_a)

    # Если размер матрицы равен 1, то просто умножаем элементы
    if n == 1:
        return [[matrix_a[0][0] * matrix_b[0][0]]]

    # Разделяем матрицы на подматрицы
    matrix_a11 = [row[:n//2] for row in matrix_a[:n//2]]
    matrix_a12 = [row[n//2:] for row in matrix_a[:n//2]]
    matrix_a21 = [row[:n//2] for row in matrix_a[n//2:]]
    matrix_a22 = [row[n//2:] for row in matrix_a[n//2:]]

    matrix_b11 = [row[:n//2] for row in matrix_b[:n//2]]
    matrix_b12 = [row[n//2:] for row in matrix_b[:n//2]]
    matrix_b21 = [row[:n//2] for row in matrix_b[n//2:]]
    matrix_b22 = [row[n//2:] for row in matrix_b[n//2:]]

    # Вычисляем промежуточные матрицы
    m1 = strassen(add(matrix_a11, matrix_a22), add(matrix_b11, matrix_b22))
    m2 = strassen(add(matrix_a21, matrix_a22), matrix_b11)
    m3 = strassen(matrix_a11, subtract(matrix_b12, matrix_b22))
    m4 = strassen(matrix_a22, subtract(matrix_b21, matrix_b11))
    m5 = strassen(add(matrix_a11, matrix_a12), matrix_b22)
    m6 = strassen(subtract(matrix_a21, matrix_a11), add(matrix_b11, matrix_b12))
    m7 = strassen(subtract(matrix_a12, matrix_a22), add(matrix_b21, matrix_b22))

    # Вычисляем результат
    c11 = add(subtract(add(m1, m4), m5), m7)
    c12 = add(m3, m5)
    c21 = add(m2, m4)
    c22 = add(subtract(add(m1, m3), m2), m6)

    # Объединяем подматрицы в одну матрицу
    result = [[0]*n for _ in range(n)]
    for i in range(n//2):
        for j in range(n//2):
            result[i][j] = c11[i][j]
            result[i][j+n//2] = c12[i][j]
            result[i+n//2][j] = c21[i][j]
            result[i+n//2][j+n//2] = c22[i][j]

    return result

def add(matrix_a, matrix_b):
    n = len(matrix_a)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result

def subtract(matrix_a, matrix_b):
    n = len(matrix_a)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix_a[i][j] - matrix_b[i][j]
    return result

result = strassen(matrix_a, matrix_b)
print(result)
