#Write a Program to illustrate following numpy array attributes.
#ndarray.ndim
#ndarray.shape
#ndarray.size
#ndarray.dtype
#ndarray.itemsize
#ndarray.data

import numpy as np
def info(arr):
    print("Array:", arr)
    print("Number of dimensions:", arr.ndim)
    print("Dimensions:", arr.shape)
    print("Total number of elements:", arr.size)
    print("Data type of elements:", arr.dtype)
    print("Size of each element in bytes:", arr.itemsize)
    print("Buffer containing the elements:", arr.data)
arr = np.array([[1, 2, 3], [4, 5, 6]])
info(arr)
