"""
Формулировка задачи: Необходимо написать функции для фильтрации изображений на ЦПУ и на ГПУ. Фильтр может быть выбран произвольно.
Решение:
Для решения этой задачи использовала библиотеку OpenCV для обработки изображений на CPU и 
библиотеку CuPy для обработки изображений на GPU. 
"""

# Функция для фильтрации изображений на CPU
import cv2

def cpu_filter(image_path, filter_type):
    # Чтение изображения
    image = cv2.imread(image_path)

    # Применение фильтра
    if filter_type == 'blur':
        filtered_image = cv2.blur(image, (5, 5))
    elif filter_type == 'gaussian':
        filtered_image = cv2.GaussianBlur(image, (5, 5), 0)
    elif filter_type == 'median':
        filtered_image = cv2.medianBlur(image, 5)
    else:
        raise ValueError("Unsupported filter type")

    return filtered_image


# Функция для фильтрации изображений на GPU:
import cupy as cp
import cv2

def gpu_filter(image_path, filter_type):
    # Чтение изображения
    image = cv2.imread(image_path)

    # Перенос изображения на GPU
    image_gpu = cp.asarray(image)

    # Применение фильтра
    if filter_type == 'blur':
        filtered_image_gpu = cp.mean(cp.lib.stride_tricks.as_strided(image_gpu, shape=(image_gpu.shape[0]-4, image_gpu.shape[1]-4, 5, 5), strides=image_gpu.strides*2), axis=(2, 3))
    elif filter_type == 'gaussian':
        kernel = cp.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]]) / 256
        filtered_image_gpu = cp.fft.ifft2(cp.fft.fft2(image_gpu) * cp.fft.fft2(cp.pad(kernel, ((image_gpu.shape[0]//2-2, image_gpu.shape[0]//2-2), (image_gpu.shape[1]//2-2, image_gpu.shape[1]//2-2)), mode='constant')).real
    elif filter_type == 'median':
        filtered_image_gpu = cp.median(cp.lib.stride_tricks.as_strided(image_gpu, shape=(image_gpu.shape[0]-4, image_gpu.shape[1]-4, 5, 5), strides=image_gpu.strides*2), axis=(2, 3))
    else:
        raise ValueError("Unsupported filter type")

    # Перенос изображения обратно на CPU
    filtered_image = cp.asnumpy(filtered_image_gpu)

    return filtered_image
