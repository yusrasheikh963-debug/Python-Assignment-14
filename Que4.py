import numpy as np

arr = np.arange(1, 25)    # Create a 1D array from 1 to 24

print("Original Array:")
print(arr)
print("Shape:", arr.shape)

arr1 = arr.reshape(4, 6)   # Reshape into (4, 6)
print("\nReshaped to (4, 6):")
print(arr1)
print("Shape:", arr1.shape)

arr2 = arr.reshape(3, 8)   # Reshape into (3, 8)
print("\nReshaped to (3, 8):")
print(arr2)
print("Shape:", arr2.shape)

arr3 = arr.reshape(2, 3, 4)    # Reshape into (2, 3, 4) - 3D Array
print("\nReshaped to (2, 3, 4):")
print(arr3)
print("Shape:", arr3.shape)