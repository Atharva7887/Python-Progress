def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# Importing from another file

# NumPy Basics
import numpy as np

# Create arrays
arr = np.array([1, 2, 3, 4])
print("Array:", arr)

# 2D Array
matrix = np.array([[1, 2], [3, 4]])
print("2D Array:\n", matrix)

# Array operations
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Sum:", np.sum(arr))
print("Reshape to 2x2:\n", arr.reshape(2, 2))
