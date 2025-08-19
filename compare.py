import numpy as np

# Example arrays
a = np.array([1, 2, 3, 4])
b = np.array([2, 2, 1, 5])

# Element-wise comparisons
greater = a > b
greater_equal = a >= b
lesser = a < b

# Display results
print("Array a:", a)
print("Array b:", b)
print("a > b:", greater)
print("a >= b:", greater_equal)
print("a < b:", lesser)
