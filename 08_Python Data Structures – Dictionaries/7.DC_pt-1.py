# ------------------------------------------------------------
# ----------**## Dictionary Comprehensions Part 1 ##**--------


# ******------****** Example 26

# coordinates = {}
# for x in range(5):
#   coordinates[x] = (((x * 5) / 2) + 12) - (2.4 / 1.2) * 6


# coordinates = {x: (((x * 5) / 2) + 12) - (2.4 / 1.2) * 6 for x in range(5)}

# print(coordinates)


# ******------****** Example 27

# items prices in Dollars
# old_price = {"milk": 1.02, "coffee": 2.5, "bread": 1.89}

# dollar_to_pound = 0.76
# new_price = {item: value * dollar_to_pound for (item, value) in old_price.items()}

# print(new_price)


# ******------****** Example 28 ->>>> If Conditional Dictionary Comprehension

original_dict = {'Jack': 38, 'Lincoln': 48,
                 'Theodore': 57, 'John': 33, "Cecile": 21, "Tony": 18}

even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)
