""""
Write a Program to demonstrative NumPy Arrays Creation Functions: -
np.zeros() Creates an array of zeros
np.ones() Creates an array of ones
np.empty() Creates an empty array
np.full() Creates a full array
np.eye() Creates an identity matrix
np.random. random() Creates an array with random values
"""


import numpy as np
# np.zeros() - Creates an array of zeros
zeros_array = np.zeros((2, 3))
print("Array of zeros:")
print(zeros_array)

# np.ones() - Creates an array of ones
ones_array = np.ones((2, 3))
print("\nArray of ones:")
print(ones_array)

# np.empty() - Creates an empty array
empty_array = np.empty((2, 2))
print("\nEmpty array:")
print(empty_array)

# np.full() - Creates a full array
full_array = np.full((3, 3), 5)     #(3,3)  dt imension of array 5:value of each element
print("\nFull array with value 5:")
print(full_array)

# np.eye() - Creates an identity matrix
identity_matrix = np.eye(4)
print("\nIdentity matrix:")
print(identity_matrix)

# np.random.random() - Creates an array with random values
random_array = np.random.random((3, 3))
print("\nArray with random values:")
print(random_array)
