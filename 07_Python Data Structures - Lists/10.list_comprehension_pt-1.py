# ------------------------------------------------------------
# ------------**## List Comprehensions Part 1 ##**------------

# Basic syntax of an LC
# [expression for item in list]

numbers = [23, 54, 67, 89, 15, 99]
fruits = ['Apple', "Orange", "Banana"]


# ******------****** Example 36

# numbers2 = [num for num in numbers]
# print(numbers2)


# ******------****** Example 37

# numbers2 = [num*2 for num in numbers]
# print(numbers2)

# ******------****** Example 38

# numbers2 = [(num / 2) * 5 for num in numbers]
# print(numbers2)


# ******------****** Example 39

# fruits2 = [fruit.lower() for fruit in fruits]
# print(fruits2)

# ******------****** Example 40

products = [
    ("Cup", 5),
    ("T-Shirt", 19),
    ("Hat", 29),
    ("Watch", 49),
    ("UV Lamp", 27),
    ("Mug", 7),
]

items = [item for item in products]
items = [item[0] for item in products]
items = [item[1] for item in products]
print(items)
