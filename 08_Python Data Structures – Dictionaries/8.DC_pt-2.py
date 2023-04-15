# ------------------------------------------------------------
# ----------**## Dictionary Comprehensions Part 2 ##**--------


# ******------****** Example 29 ->>>> Multiple if Conditional Dictionary Comprehension

original_dict = {'Jack': 38, 'Lincoln': 48,
                 'Theodore': 57, 'John': 33, "Cecile": 21, "Tony": 18}


# new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
# print(new_dict)

# ******------****** Example 30 ->>>> if-else Conditional Dictionary Comprehension

# new_dict = {k: "old" if v > 40 else "young" for (k, v) in original_dict.items()}

# print(new_dict)


# ******------****** Example 31 ->>>> Nested Dictionary with Two Dictionary Comprehensions

# new_dict = {
#     k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
# }

# print(new_dict)

# ******------****** Example 32 ->>>> Nested Dictionary with Two Dictionary Comprehensions in the loop form

# new_dict = {}
# for k1 in range(2, 5):
#   new_dict[k1] = {k2: k1 * k2 for k2 in range(1, 6)}

# print(new_dict)


# ******------****** Example 33 ->>>> Nested Dictionary with Two Dictionary Comprehensions in the loop form, completely unfolded

new_dict = {}
for k1 in range(2, 5):
    new_dict[k1] = {}
    for k2 in range(1, 6):
        new_dict[k1][k2] = k1 * k2

print(new_dict)
