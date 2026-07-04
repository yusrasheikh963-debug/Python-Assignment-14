import numpy as np

A = np.array([[1, 2, 3],    # Create two 3*3 matrices
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

element_wise = A * B  # Element-wise multiplication
matrix_mul = A @ B   # Matrix multiplication

print("\nMatrix A:", A)
print("Matrix B:", B)

print("\nElement-wise Multiplication:")
print(element_wise)

print("Matrix Multiplication:")
print(matrix_mul)
