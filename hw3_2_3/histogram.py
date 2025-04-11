"""
Формулировка задания: 
1. необходимо написать функции для вывода гистограммы черно-белого изображения на ЦПУ и ГПУ;
2. необходимо сравнить скорости двух реализаций (например с использованием библиотеки cupy или придумать свои методы . 
"""

"""
Решение:
Для решения этой задачи, я использовала библиотеку OpenCV для обработки изображений на CPU и библиотеку CuPy для обработки изображений на GPU. 
"""

# Функция для вывода гистограммы на CPU
import cv2
import numpy as np
import matplotlib.pyplot as plt

def cpu_histogram(image_path):
    # Чтение изображения
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Вычисление гистограммы
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Вывод гистограммы
    plt.plot(hist)
    plt.show()

# Функция для вывода гистограммы на GPU
import cv2
import cupy as cp
import matplotlib.pyplot as plt

def gpu_histogram(image_path):
    # Чтение изображения
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Перенос изображения на GPU
    image_gpu = cp.asarray(image)

    # Вычисление гистограммы
    hist_gpu = cp.zeros(256, dtype=cp.int32)
    for i in range(256):
        hist_gpu[i] = cp.sum(image_gpu == i)

    # Перенос гистограммы обратно на CPU
    hist = cp.asnumpy(hist_gpu)

    # Вывод гистограммы
    plt.plot(hist)
    plt.show()

# Сравнение скоростей двух реализаций
import time

start_time = time.time()
cpu_histogram('image_path')
cpu_time = time.time() - start_time

start_time = time.time()
gpu_histogram('image_path')
gpu_time = time.time() - start_time

print(f'CPU time: {cpu_time}')
print(f'GPU time: {gpu_time}')

