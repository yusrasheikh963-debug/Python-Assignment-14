import numpy as np

arr = np.array([[10, 20, 30, 40],    # Create a 2D array
                [50, 60, 70, 80],
                [90, 100, 110, 120]])

print("\nOriginal Array:")
print(arr)

print("\nFirst Row:")   # Extract first row
print(arr[0])

print("Last Column:")    # Extract last column
print(arr[:, 3])

print("Center 2x2 Submatrix:")   # Extract center 2x2 submatrix
print(arr[1:3, 1:3])

print("Even Numbers:")    # Extract all even numbers using boolean indexing
print(arr[arr % 2 == 0])