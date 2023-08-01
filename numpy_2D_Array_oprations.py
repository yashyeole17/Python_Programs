"""
Create two 2-d Numpy Arrays (Matrix A, Matrix B) and perform the␣following operation on matrix
a. Addition ( A+B)
b. Multiplication ( AxB)
c. Scalar Multiplication (A x integer or integer x A)
d. Transpose of Matrix
"""

import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6]])       # matrix A
B = np.array([[7, 8, 9], [10, 11, 12]])       # matrix B

addition = A + B
print("Addition (A + B):")
print(addition)

# Multiplication
multiplication = np.dot(A, B.T)
print("\nMultiplication (A x B^T):")
print(multiplication)

# Scalar Multiplication
scalar = 2
scalar_multiplication_A = A * scalar
scalar_multiplication_B = scalar * B

print("\nScalar Multiplication (A x", scalar, "):")
print(scalar_multiplication_A)
print("\nScalar Multiplication (", scalar, "x B):")
print(scalar_multiplication_B)

# Transpose
transpose_A = A.T
transpose_B = B.T
print("\nTranspose of Matrix A:")

print(transpose_A)
print("\nTranspose of Matrix B:")
print(transpose_B)
