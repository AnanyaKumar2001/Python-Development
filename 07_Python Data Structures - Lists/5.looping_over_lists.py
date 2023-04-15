# ------------------------------------------------------------
# -----------------**## Looping Over Lists ##**---------------


# ******------****** Example 16

letters = ["a", "b", "c"]

# for letter in letters:
#     print(letter)


# ******------****** Example 17

# for letter in enumerate(letters):
#     print(letter)


# ******------****** Example 18

# items = (0, "a")
# index, letter = items
# print(index, letter)

# ******------****** Example 19

for index, item in enumerate(letters):
    print(index, item)
