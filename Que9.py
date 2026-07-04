import numpy as np

arr = np.random.randn(6, 6)   # Generate a 6x6 matrix using np.random.randn()
print("Original Matrix:")
print(np.round(arr, 4))   # rounded for readability

print("\nShape:", arr.shape)   # Print shape of the matrix
print("Size:", arr.size)       # Print size of the matrix
print("Data type:", arr.dtype) # Print data type of the matrix

max_index = np.unravel_index(arr.argmax(), arr.shape)   # Find index of maximum value
min_index = np.unravel_index(arr.argmin(), arr.shape)   # Find index of minimum value

print("\nIndex of Maximum Value:", max_index)
print("Index of Minimum Value:", min_index)

print("\nTop-left 3x3 Submatrix:")   # Extract top-left 3x3 submatrix
print(np.round(arr[:3, :3], 4))

arr_modified = np.abs(arr)   # Replace negative numbers with absolute values
print("\nModified Matrix (Absolute values):")
print(np.round(arr_modified, 4))

print("\nMean of Modified Matrix:", round(arr_modified.mean(), 4))  # Mean of modified matrix