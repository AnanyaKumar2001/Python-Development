# ------------------------------------------------------------
# ------------**## List Comprehensions Part 2 ##**------------


products = [
    ("Cup", 5),
    ("T-Shirt", 20),
    ("Hat", 29),
    ("Watch", 49),
    ("UV Lamp", 27),
    ("Mug", 7),
]


numbers = [21, 24, 56, 564, 102, 321, 79, 84, 222, 111, 100]

# ******------****** Example 41 ->>>> Single Condition

# items = [item[1] for item in products if item[1] >= 20]
# print(items)


# ******------****** Example 42 ->>>> Two Conditions

modified_numbers = [num if num > 100 else num / 2 for num in numbers]
modified_numbers = [num if num < 100 else num / 2 for num in numbers]

print(modified_numbers)
