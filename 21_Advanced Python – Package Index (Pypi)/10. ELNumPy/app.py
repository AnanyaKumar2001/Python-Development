# ****************------------------- NumPy

# pipenv install numpy

import numpy as np


# *-*-*-*-*-*-*-*-*-*-*-*- Creating a simple array
# array = np.array([1, 2, 3])
# print(array)
# print(type(array))


# *-*-*-*-*-*-*-*-*-*-*-*- Creating a multidimensional array
# array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(array)

# print(array.shape)

# *-*-*-*-*-*-*-*-*-*-*-*- NumPy Helper Methods -------------------------

# -*-*-*- zeros()
# array = np.zeros((4, 6))
# print(array)

# -*-*-*- ones()
# array = np.ones((4, 6), dtype=int)
# print(array)

# -*-*-*- full()
# array = np.full((4, 6), 11, dtype=int)
# print(array)

# -*-*-*- random.random()
# array = np.random.random((3, 2))
# print(array)

# accessing the number at the first row and first col
# print(array[0, 0])

# using a comparison operator
# print(array > 0.5)

# boolean indexing
# print(array[array > 0.3])

# *-*-*-*-*-*-*-*-*-*-*-*- Array Computational Functions ---------------------------

# array = np.array([2.1, 3.9, 5.5, 11.8, 15.7, 13.3])
# print(array)

# -*-*-*- sum()
# print(np.sum(array))

# -*-*-*- floor()
# print(np.floor(array))


# -*-*-*- ceil()
# print(np.ceil(array))


# -*-*-*- round()
# print(np.round(array))


# *-*-*-*-*-*-*-*-*-*-*-*- Performing Arithmetic Operations Between Numbers and Arrays

first_array = np.array([111, 333, 555])
second_array = np.array([222, 444, 666])

print(first_array + second_array)

print(first_array + 1)

# *-*-*-*-*-*-* Unit Conversion (Legnth)
feet = np.array([1, 2, 3, 4, 5])
cm = feet * 30.48
inch = feet * 12
meter = feet * 0.3048
yard = feet * 0.3333
print(cm)
print(inch)
print(meter)
print(yard)
