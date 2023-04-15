# ------------------------------------------------------------
# ------------------**## Changing Tuples ##**-----------------


# ******------****** Example 11 ->>>> changing tuple elements

numbers = (4, 2, 3, [5, 6, 7, 8])
# numbers[1] = 10 # TypeError

# print(numbers)
numbers[3][2] = 111
# print(numbers)


# ******------****** Example 12 ->>>> reassignment of a tuple

numbers = (222, 333, 444)
# print(numbers)


# ******------****** Example 13 ->>>> repeating a tuple items

# print(("Movie",) * 5)


# ******------****** Example 14 ->>>> tuple concatenation

letters = ("p", "y", "t", "h", "o", "n")

# mixed = numbers + letters
# print(mixed)


# ******------****** Example 15 ->>>> deleting a tuple entirely

del letters

# print(letters) # NameError
