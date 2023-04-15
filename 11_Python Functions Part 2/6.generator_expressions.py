# ------------------------------------------------------------
# ---------------**## Generator Expressions ##**--------------

from sys import getsizeof

# ******------****** Example 13 ->>>> list comprehension

# numbers = [x * 2 for x in range(15)]
# print(numbers)
# print(type(numbers))

# for x in numbers:
#   print(x)


# ******------****** Example 14 ->>>> generator object

# numbers = (x * 2 for x in range(15))
# print(numbers)
# print(type(numbers))

# for y in numbers:
#   print(y)


# ******------****** Example 15 ->>>> getting the size of a generator object

numbers_gen = (x * 2 for x in range(10))
numbers_gen = (x * 2 for x in range(100))
numbers_gen = (x * 2 for x in range(1000))
numbers_gen = (x * 2 for x in range(10000))
numbers_gen = (x * 2 for x in range(100000))
numbers_gen = (x * 2 for x in range(1000000))


print("GO:", getsizeof(numbers_gen))  # 112 bytes

# ******------****** Example 16 ->>>> getting the size of a list comprehension

numbers_list = [x * 2 for x in range(10)]
numbers_list = [x * 2 for x in range(100)]
numbers_list = [x * 2 for x in range(1000)]
numbers_list = [x * 2 for x in range(10000)]
numbers_list = [x * 2 for x in range(100000)]
numbers_list = [x * 2 for x in range(1000000)]


print("LCE:", getsizeof(numbers_list))
