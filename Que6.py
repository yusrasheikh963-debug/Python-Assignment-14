import numpy as np

arr = np.random.randint(1, 101, (5, 5))   # Create a 5*5 matrix

print("Original Matrix:")
print(arr)

print("\nDiagonal Elements:")   # Print diagonal elements
print(np.diagonal(arr))

print("\nElements Greater Than 50:")   # Print elements greater than 50
print(arr[arr > 50])

arr[arr < 30] = 0   # Replace all elements less than 30 with 0

print("\nModified Matrix:")   # Print the modified matrix
print(arr)