# ------------------------------------------------------------
# -----------------**## Sets Introduction ##**----------------


# ******------****** Example 1

# first_set = {21, 32, 54, 665, 999}
# print(first_set)


# ******------****** Example 2
# mixed = {5.19, "Set", ("London", "Paris")}
# print(mixed)


# ******------****** Example 3
# numbers = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5 ,6}
# print(numbers)


# ******------****** Example 4 ->>>> creating a set from a tuple

# colors = set(("blue", "red", "green", "blue"))
# print(colors)


# ******------****** Example 5 ->>>> creating a set from a list

# colors = set(["blue", "red", "green", "blue"])
# print(colors)

# ******------****** Example 6 ->>>> creating a set from a dict

# colors = set({
#     "blue": 1,
#     "red": 2,
#     "green": 3
# })

# print(colors)

# ******------****** Example 7 ->>>> a set cannot have a mutable data type as an item

# colors = {"red", "blue", [1, 2, 3]} # TypeError


# ******------****** Example 8 ->>>> creating an empty set

names = {}
print(names)
print(type(names))

numbers = set()
print(numbers)
print(type(numbers))
