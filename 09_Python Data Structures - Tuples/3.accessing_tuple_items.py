# ------------------------------------------------------------
# ---------------**## Accessing Tuple Items ##**--------------


# ******------****** Example 8 ->>>> Indexing

mixed = (False, 3.14159, "Python", ["Web", "Mobile"], 45)
# print(mixed[0])
# print(mixed[2])
# print(mixed[5]) # IndexError
# print(mixed["a"]) # TypeError


# ******------****** Example 9 ->>>> Negative Indexing
# print(mixed[-1])
# print(mixed[-2])
# print(mixed[-4])
# print(mixed[-5])

# ******------****** Example 10 ->>>> Slicing

# print(mixed[0:2])
# print(mixed[2:4])
# print(mixed[:4])
# print(mixed[3:])
# print(mixed[:])
print(mixed[:-1])
print(mixed[:-3])
