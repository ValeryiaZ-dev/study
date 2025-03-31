#include <iostream>
#include <cstdlib>
#include <ctime>
#include "matrix_operation.h"

using namespace std;

int main() {
    int firstMatrix[512][512], secondMatrix[512][512], result[512][512];
    int vector[512], resultVector[512];

    // Инициализация генератора случайных чисел
    srand(time(0));

    // Заполнение матриц и вектора рандомными числами
    for (int i = 0; i < 512; ++i) {
        for (int j = 0; j < 512; ++j) {
            firstMatrix[i][j] = rand() % 100;
            secondMatrix[i][j] = rand() % 100;
        }
        vector[i] = rand() % 100;
    }

    multiplyMatrices(firstMatrix, secondMatrix, result, 512, 512, 512, 512);

    cout << "Результат умножения матриц: " << endl;
    for (int i = 0; i < 512; ++i)
        for (int j = 0; j < 512; ++j) {
            cout << result[i][j] << "  ";
            if (j == 511)
                cout << endl;
        }

    multiplyMatrixByVector(firstMatrix, vector, resultVector, 512, 512);

    cout << "Результат умножения матрицы на вектор: " << endl;
    for (int i = 0; i < 512; ++i) {
        cout << resultVector[i] << "  ";
    }

    return 0;
}

