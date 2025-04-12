#include "matrix_operations.h"
#include <iostream>
#include <chrono>
#include <math.h>

int main() {
    int N = 4096;
    double* A = new double[N * N];
    double* B = new double[N * N];
    double* C = new double[N * N];
    double* C_strassen = new double[N * N];

    // Инициализация матриц и векторов
    for (int i = 0; i < N * N; ++i) {
        A[i] = static_cast<double>(rand()) / RAND_MAX;
        B[i] = static_cast<double>(rand()) / RAND_MAX;
    }

    // Измерение времени для умножения матриц
    auto start = std::chrono::high_resolution_clock::now();
    matrix_multiply(A, B, C, N);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << "BLAS matrix multiplication time: " << elapsed.count() << " s\n";
    
    start = std::chrono::high_resolution_clock::now();
    strassen(A, B, C_strassen, N);
    end = std::chrono::high_resolution_clock::now();
    elapsed = end - start;
    std::cout << "Strassen matrix multiplication time: " << elapsed.count() << " s\n";
    
    double error = calculate_error(C, C_strassen, N*N);
    std::cout << "Max error: " << error << "\n";
    delete[] A;
    delete[] B;
    delete[] C;
    delete[] C_strassen;

    return 0;
}
