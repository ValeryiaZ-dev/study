"""
Формулировка задания: сгенерировать случайные разреженные графы и сравнить 
производительность реализаций Pagerank с CSR-форматом и без него.
"""

import networkx as nx
import numpy as np
import time

# Генерируем случайный разреженный граф
N = 1000
p = 0.01
G = nx.gnp_random_graph(N, p)

# Вычисляем PageRank без CSR-формата
start_time = time.time()
pagerank = nx.pagerank(G)
end_time = time.time()
print(f'PageRank без CSR-формата: {end_time - start_time} секунд')

# Преобразуем граф в CSR-формат
csr_matrix = nx.to_scipy_sparse_array(G, format='csr')

# Вычисляем PageRank с CSR-форматом - (не получилось сделать!)
start_time = time.time()
pagerank_csr = nx.pagerank(csr_matrix, max_iter=100)
end_time = time.time()
print(f'PageRank с CSR-форматом: {end_time - start_time} секунд')
