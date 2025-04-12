#include "matrix_operations.h"
#include <cblas.h>
#include <math.h>

void matrix_multiply(double* A, double* B, double* C, int N) {
    cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans, N, N, N, 1.0, A, N, B, N, 0.0, C, N);
}

double calculate_error(double* C1, double* C2, size_t length) {
    double max_error = 0.0;
    for (size_t i = 0; i < length; i++) {
        double error = fabs(C1[i] - C2[i]);
        if (error > max_error) {
            max_error = error;
        }
    }
    return max_error;
}

void add(double* A, double* B, double* C, size_t length) {
    for (size_t i = 0; i < length; i++) {
        C[i] = A[i] + B[i];
    }
    return;
}

void subtract(double* A, double* B, double* C, size_t length) {
    for (size_t i = 0; i < length; i++) {
        C[i] = A[i] - B[i];
    }
    return;
}

// Основная функция Штрассена с одномерными массивами
void strassen(double* A, double* B, double* C, size_t N) {
    if (N <= 64) {
        matrix_multiply(A, B, C, N);
        return;
    }

    size_t K = N / 2;
    double* temp1 = new double [K*K];
    double* temp2 = new double [K*K];
    
    double* M1 = new double [K*K];
    // A11 + A22 and B11 + B22
    for (size_t i = 0; i < K; i++) {
        add(A+i*N, A+N*K+K+i*N, temp1+i*K, K);
        add(B+i*N, B+N*K+K+i*N, temp2+i*K, K);
    }
    strassen(temp1, temp2, M1, K);
    
    double* M2 = new double [K*K];
    // A21 + A22 and B11
    for (size_t i = 0; i < K; i++) {
        add(A+N*K+i*N, A+N*K+K+i*N, temp1+i*K, K);
        for (size_t j = 0; j < K; j++)
            temp2[i*K+j] = B[i*N+j];
    }
    strassen(temp1, temp2, M2, K);

    double* M3 = new double [K*K];
    // A11 and B12 - B22
    for (size_t i = 0; i < K; i++) {
        for (size_t j = 0; j < K; j++)
            temp1[i*K+j] = A[i*N+j];
        subtract(B+K+i*N, B+N*K+K+i*N, temp2+i*K, K);
    }
    strassen(temp1, temp2, M3, K);

    double* M4 = new double [K*K];
    // A22 and B21 - B11
    for (size_t i = 0; i < K; i++) {
        for (size_t j = 0; j < K; j++)
            temp1[i*K+j] = A[N*K+K+i*N+j];
        subtract(B+N*K+i*N, B+i*N, temp2+i*K, K);
    }
    strassen(temp1, temp2, M4, K);

    double* M5 = new double [K*K];
    // A11 + A12 and B22
    for (size_t i = 0; i < K; i++) {
        add(A+i*N, A+K+i*N, temp1+i*K, K);
        for (size_t j = 0; j < K; j++)
            temp2[i*K+j] = B[N*K+K+i*N+j];
    }
    strassen(temp1, temp2, M5, K);

    double* M6 = new double [K*K];
    // A21 - A11 and B11 + B12
    for (size_t i = 0; i < K; i++) {
        subtract(A+N*K+i*N, A+i*N, temp1+i*K, K);
        add(B+i*N, B+K+i*N, temp2+i*K, K);
    }
    strassen(temp1, temp2, M6, K);
    
    double* M7 = new double [K*K];
    // A12 - A22 and B21 + B22
    for (size_t i = 0; i < K; i++) {
        subtract(A+K+i*N, A+N*K+K+i*N, temp1+i*K, K);
        add(B+N*K+i*N, B+N*K+K+i*N, temp2+i*K, K);
    }
    strassen(temp1, temp2, M7, K);
    
    
    for (size_t i = 0; i < K; i++) {
        for (size_t j = 0; j < K; j++) {
            C[i * N + j] = M1[i*K+j] + M4[i*K+j]
                          -M5[i*K+j] + M7[i*K+j];
            C[i * N + j + K] = M3[i*K+j] + M5[i*K+j];
            C[(K + i) * N + j] = M2[i*K+j] + M4[i*K+j];
            C[(K + i) * N + K + j] = M1[i*K+j] - M2[i*K+j]
                                    +M3[i*K+j] + M6[i*K+j];
        }
    }

    // Free memory
    delete[] temp1; delete[] temp2; delete[] M1; 
    delete[] M2; delete[] M3; delete[] M4;
    delete[] M5; delete[] M6; delete[] M7;
    return;

}
