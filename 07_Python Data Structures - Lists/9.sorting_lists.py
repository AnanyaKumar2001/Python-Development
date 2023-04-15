# ------------------------------------------------------------
# ------------------**## Sorting Lists ##**-------------------


numbers = [1, 5, 32, 124, 70, 854, 2356, 6589, 62, 8, 19, 999, 321]


# ******------****** Example 32 ->>>> sort()

# numbers.sort()
# numbers.sort(reverse=True)
# print(numbers)

# ******------****** Example 33 ->>>> sorted()

# print(sorted(numbers))
# print(sorted(numbers, reverse=True))


# ******------****** Example 34 ->>>> sort()

products = [
    ("Cup", 5),
    ("T-Shirt", 19),
    ("Hat", 29),
    ("Watch", 49),
    ("UV Lamp", 27),
    ("Mug", 7),
]

# products.sort()
# print(products)

# ******------****** Example 35 ->>>> sort()


def sort_products(product):
    return product[1]


products.sort(key=sort_products)
print(products)
