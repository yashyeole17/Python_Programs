#Write a Program to Basic Arithmetic Operations on NumPy Arrays.

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

add = arr1 + arr2              # Addition
subtract = arr1 - arr2         # Subtraction
mul = arr1 * arr2              # Multiplication
div = arr1 / arr2              # Division
exp = arr1 ** arr2             # Exponentiation
mod = arr1 % arr2              # Modulo

print("Addition:", add)
print("Subtraction:", subtract)
print("Multiplication:", mul)
print("Division:", div)
print("Exponentiation:", exp)
print("Modulo:", mod)