# ------------------------------------------------------------
# -----------------**## Unpacking Operator ##**---------------

# * -> unpacking operator

# ******------****** Example 17
# numbers = [1, 2, 3]
# print(numbers)

# print(1, 2, 3)
# print(*numbers)

# ******------****** Example 18

# values = list(range(15))
# print(values)
# print(*values)


# values = [*range(20)]
# print(*values)

# print({*"Python"})

# ******------****** Example 19

# cities = ["Rome", "Athens", "Istanbul", "Tokyo", "Jakarta"]
# names = ["Olivia", "Amelia", "Oliver", "Charlotte", "Liam"]

# info = [*names, *cities]
# print(info)


# ******------****** Example 20

dict_one = {
    "name": "Jasper",
    "city": "Tokyo"
}

dict_two = {
    "full name": "Dick Van Dyke",
    "address": "USA"
}

dict_three = {
    "name": "William",
    "job": "Developer"
}


combined = {**dict_one, **dict_two, "Country": "France", **dict_three}
print(combined)
