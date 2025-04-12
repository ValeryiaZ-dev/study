#ifndef MATRIX_OPERATIONS_H
#define MATRIX_OPERATIONS_H
#include <math.h>

void matrix_multiply(double* A, double* B, double* C, int N);
double calculate_error(double* C1, double* C2, size_t length);
void add(double* A, double* B, double* C, size_t length);
void subtract(double* A, double* B, double* C, size_t length);
void strassen(double* A, double* B, double* C, size_t N);

#endif
