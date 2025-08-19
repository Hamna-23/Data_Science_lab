# Element-wise multiplication using a loop

def multiply_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Arrays must be of the same length")

    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] * arr2[i])
    return result

# Example usage
a = [2, 4, 6]
b = [3, 5, 7]
product = multiply_arrays(a, b)
print("Result:", product)
