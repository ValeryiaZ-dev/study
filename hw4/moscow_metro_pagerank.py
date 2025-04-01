"""
Формулировка задания:
1) найти и подготовить датасет Московского или Лондонского метро для решения стандартной задачи Pagerank.
Вывести топ-5 станций подземки по такому ранжированию.
2) применить метод Simrank к графу Московской подземки.
"""

import requests
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Читаем CSV-файл
df = pd.read_csv('/Users/19992974/IdeaProjects/bio_sdk/dz4/metro.csv', sep=';', encoding='cp1251')
print(df)

# Исключаем первый и второй столбцы, а также первую строку
df = df.iloc[1:, 2:]

# Преобразуем DataFrame в матрицу
matrix = df.values

# Преобразуем все ненулевые значения в 1
matrix = np.where(matrix != 0, 1, matrix)
print(matrix)

# Создаем граф на основе матрицы
G = nx.from_numpy_array(matrix)

'''
# Визуализируем граф
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()
'''

# Вычисляем PageRank
pagerank = nx.pagerank(G)

# Выводим топ 5 станций по PageRank
top_5 = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:5]
for station, rank in top_5:
    print(f'Station: {station}, PageRank: {rank}')

# Вычисляем SimRank
N = matrix.shape[0]
G = nx.cycle_graph(N)
simrank = nx.simrank_similarity(G)
for i in range(N):
    for j in range(i):
        print('source=', i, 'target=', j, 'similarity=', simrank[i][j])
simrank = nx.simrank_similarity(G)
