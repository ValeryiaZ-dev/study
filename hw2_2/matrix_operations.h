#ifndef MATRIX_OPERATIONS_H
#define MATRIX_OPERATIONS_H

#include <iostream>

void multiplyMatrices(int firstMatrix[][512], int secondMatrix[][512], int result[][512], int rowFirst, int columnFirst, int rowSecond, int columnSecond);
void multiplyMatrixByVector(int matrix[][512], int vector[], int result[], int row, int column);

#endif // MATRIX_OPERATIONS_H
