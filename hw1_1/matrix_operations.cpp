// Формулировка задания: Реализовать на языке C/C++ классические операции перемножения квадратных матриц и умножения матрицы на вектор

#include <iostream>

using namespace std;

// Функция для умножения двух квадратных матриц
void multiplyMatrices(int firstMatrix[][10], int secondMatrix[][10], int result[][10], int rowFirst, int columnFirst, int rowSecond, int columnSecond) {
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

// Функция для умножения матрицы на вектор
void multiplyMatrixByVector(int matrix[][10], int vector[], int result[], int row, int column) {
    // Инициализация результата нулями
    for (int i = 0; i < row; ++i)
        result[i] = 0;

    // Умножение матрицы на вектор
    for (int i = 0; i < row; ++i)
        for (int j = 0; j < column; ++j) {
            result[i] += matrix[i][j] * vector[j];
        }
}

int main() {
    int firstMatrix[10][10], secondMatrix[10][10], result[10][10], rowFirst, columnFirst, rowSecond, columnSecond;

    cout << "Введите количество строк и столбцов первой матрицы: ";
    cin >> rowFirst >> columnFirst;

    cout << "Введите элементы первой матрицы: " << endl;
    for (int i = 0; i < rowFirst; ++i)
        for (int j = 0; j < columnFirst; ++j) {
            cin >> firstMatrix[i][j];
        }

    cout << "Введите количество строк и столбцов второй матрицы: ";
    cin >> rowSecond >> columnSecond;

    cout << "Введите элементы второй матрицы: " << endl;
    for (int i = 0; i < rowSecond; ++i)
        for (int j = 0; j < columnSecond; ++j) {
            cin >> secondMatrix[i][j];
        }

    // Проверка, можно ли умножить матрицы
    if (columnFirst != rowSecond) {
        cout << "Ошибка! Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы." << endl;
        return -1;
    }

    multiplyMatrices(firstMatrix, secondMatrix, result, rowFirst, columnFirst, rowSecond, columnSecond);

    cout << "Результат умножения матриц: " << endl;
    for (int i = 0; i < rowFirst; ++i)
        for (int j = 0; j < columnSecond; ++j) {
            cout << result[i][j] << "  ";
            if (j == columnSecond - 1)
                cout << endl;
        }

    int vector[10], resultVector[10];

    cout << "Введите элементы вектора: " << endl;
    for (int i = 0; i < columnFirst; ++i) {
        cin >> vector[i];
    }

    multiplyMatrixByVector(firstMatrix, vector, resultVector, rowFirst, columnFirst);

    cout << "Результат умножения матрицы на вектор: " << endl;
    for (int i = 0; i < rowFirst; ++i) {
        cout << resultVector[i] << "  ";
    }

    return 0;
}
