#ifndef MATRIX_OPERATIONS_H
#define MATRIX_OPERATIONS_H

#include <iostream>

void multiplyMatrices(int firstMatrix[][10], int secondMatrix[][10], int result[][10], int rowFirst, int columnFirst, int rowSecond, int columnSecond);
void multiplyMatrixByVector(int matrix[][10], int vector[], int result[], int row, int column);

#endif // MATRIX_OPERATIONS_H
