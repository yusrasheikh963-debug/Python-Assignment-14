import numpy as np

arr = np.random.randint(1, 51, 20)    # Generate 20 random integers between 1 and 50
print("\nArray:", arr)   # Print the array

print("Minimum value:", arr.min())   # Minimum value and its index
print("Index of minimum value:", arr.argmin())

print("Maximum value:", arr.max())   # Maximum value and its index
print("Index of maximum value:", arr.argmax())

print("Sum of all elements:", arr.sum())   # Sum of all elements
print("Mean:", arr.mean())   # Mean

print("Standard Deviation:", arr.std())   # Standard Deviation