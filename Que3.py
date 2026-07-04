import numpy as np

matrix = np.random.randint(20, 81, (4, 5))   # Create a 4*5 matrix of random integers between 20 & 80
print("\nMatrix:\n", matrix)   # Print the matrix

print("\nMinimum value:", matrix.min())   # Minimum value
print("Maximum value:", matrix.max())   # Maximum value

print("Sum of all elements:", matrix.sum())   # Sum of all elements
print("Mean:", matrix.mean())   # Mean

print("Standard Deviation:", matrix.std())   # Standard Deviation
print("\nSum of each row:", matrix.sum(axis=1))   # Sum of each row

print("Sum of each column:", matrix.sum(axis=0))   # Sum of each column