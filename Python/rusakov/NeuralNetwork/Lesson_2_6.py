import numpy as np

# Creating a one-dimensional array
arr1: np = np.array([1, 2, 3, 4, 5])
print(arr1)

# Creating a two-dimensional array
arr2: np = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print(arr2.shape)

# Creating an array with zeros
zeros: np = np.zeros((3, 3))
print(zeros)

# Creating an array with ones
ones: np = np.ones((2, 2))
print(ones)

print(np.ones_like(zeros))

# Creating an array with random numbers
random_arr: np = np.random.rand(2, 3)
print(random_arr)

# Mathematical operations
arr3: np = np.array([1, 2, 3])
arr4: np = np.array([4, 5, 6])

result: np = arr3 + arr4
print(result)

result: np = arr3 - arr4
print(result)

result: np = arr3 * arr4
print(result)

result: np = arr3 / arr4
print(result)

# Indexing and slicing
element: np = arr1[2]
print(element)

subarray: np = arr2[0]
print(subarray)

slice: np = arr1[1:4]
print(slice)

# Indexing with a condition
mask: np = arr1 > 2
print(mask)
masked_data: np = arr1[mask]
print(masked_data)
print(arr1[arr1 > 2])

# Mathematical functions
mean: np = np.mean(arr1)
print(mean)

std: np = np.std(arr1)
print(std)

max_value: np = np.max(arr1)
print(max_value)

min_value: np = np.min(arr1)
print(min_value)

# Dot product
print(arr3)
print(arr4)

dot: np = arr3.dot(arr4)
print(dot)

arr3: np = np.array([[1, 2], [3, 4]])
arr4: np = np.array([[3, 4], [5, 6]])
print(arr3.dot(arr4))

# Matrix transposition
transposed: np  =arr2.T
print(arr2)
print(transposed)
print(transposed.T)
