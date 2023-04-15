# ------------------------------------------------------------
# ------------**## Modifying List Items Part 1 ##**-----------


numbers = [1, 55, 64, 124, 654]
names = ['John', 'Mark', 'Emily', "Sandra"]
fruits = ['Apple', "Orange", "Banana"]


# ******------****** Example 20 ->>> append()

names.append("Sandrine")
# print(names)

# ******------****** Example 21 ->>> insert()


fruits.insert(1, "Lemon")
fruits.insert(0, "Peach")
# print(fruits)


# ******------****** Example 22 ->>> pop()

# numbers.pop()
# print(numbers)

# ******------****** Example 23 ->>> pop()

# numbers.pop(-1)
# numbers.pop(1)
# names.pop(3)

# print(numbers)
# print(names)

# ******------****** Example 24 ->>> remove()

# fruits.remove("Banana")
# print(fruits)


# ******------****** Example 25 ->>> del statement

# del numbers[0]

del numbers[1:4]

print(numbers)
