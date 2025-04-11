// Формулировка задания: Реализовать на языке C/C++ классические операции перемножения квадратных матриц и умножения матрицы на 
вектор с использованием функций сторонней библиотеки BLAS.

#include <iostream>
#include <cblas.h>

int main() {
    const int N = 3; // Размер квадратной матрицы
    double A[N*N] = {1, 2, 3, 4, 5, 6, 7, 8, 9}; // Матрица A
    double B[N*N] = {9, 8, 7, 6, 5, 4, 3, 2, 1}; // Матрица B
    double C[N*N]; // Результат перемножения матриц A и B
    double X[N] = {1, 2, 3}; // Вектор X
    double Y[N]; // Результат умножения матрицы A на вектор X

    // Перемножение матриц A и B
    cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans, N, N, N, 1.0, A, N, B, N, 0.0, C, N);

    // Умножение матрицы A на вектор X
    cblas_dgemv(CblasRowMajor, CblasNoTrans, N, N, 1.0, A, N, X, 1, 0.0, Y, 1);

    // Вывод результатов
    std::cout << "Результат перемножения матриц A и B:" << std::endl;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            std::cout << C[i*N + j] << " ";
        }
        std::cout << std::endl;
    }

    std::cout << "Результат умножения матрицы A на вектор X:" << std::endl;
    for (int i = 0; i < N; i++) {
        std::cout << Y[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
