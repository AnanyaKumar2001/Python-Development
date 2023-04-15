# ------------------------------------------------------------
# -------------------**## List Unpacking ##**-----------------


# ******------****** Example 12

# numbers = [23, 49, 85]
# num1, num2, num3 = numbers
# print(num1)
# print(num2)
# print(num3)

# ******------****** Example 13

numbers = [23, 49, 85, 1, 2, 3, 4, 5]
# num1, num2, *other_nums = numbers
# print(num1)
# print(num2)
# print(other_nums)

# ******------****** Example 14

# num1, *other_nums, num2 = numbers
# print(num1)
# print(num2)
# print(other_nums)

# ******------****** Example 15

num1, num2, *other_nums, num3, num4 = numbers
print(num1)
print(num2)
print(num3)
print(num4)
print(other_nums)
