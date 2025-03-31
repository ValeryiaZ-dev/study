#include "matrix_operation.h"

void multiplyMatrices(int firstMatrix[][512], int secondMatrix[][512], int result[][512], int rowFirst, int columnFirst, int rowSecond, int columnSecond) {
    // Инициализация результата нулями
    for (int i = 0; i < rowFirst; ++i)
        for (int j = 0; j < columnSecond; ++j)
            result[i][j] = 0;

    // Умножение матриц
    for (int i = 0; i < rowFirst; ++i)
        for (int j = 0; j < columnSecond; ++j)
            for (int k = 0; k < columnFirst; ++k) {
                result[i][j] += firstMatrix[i][k] * secondMatrix[k][j];
            }
}

void multiplyMatrixByVector(int matrix[][512], int vector[], int result[], int row, int column) {
    // Инициализация результата нулями
    for (int i = 0; i < row; ++i)
        result[i] = 0;

    // Умножение матрицы на вектор
    for (int i = 0; i < row; ++i)
        for (int j = 0; j < column; ++j) {
            result[i] += matrix[i][j] * vector[j];
        }
}
