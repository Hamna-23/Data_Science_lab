import numpy as np
a = np.array([[1, 2, 3],
              [1, 5, 5]])
b = np.array([[1, 2, 0],
              [1, 3, 5]])
result = (a == b)
print("Element-wise equality:\n", result)
if result.all():
    print("Arrays are equal element-wise.")
else:
    print("Arrays are NOT equal element-wise.")
