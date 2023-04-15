# ------------------------------------------------------------
# -----------------**## Ternary Operator ##**-----------------

score = 74

# *-*-*-*-* First Version
# if score >= 75:
#   print("Passed")
# else:
#   print("Failed")


# *-*-*-*-* Second Version
# if score >= 75:
#     result = "Passed"
# else:
#     result = "Failed"

# print(result)

# *-*-*-*-* Third Version ->>> Ternary Operator
result = "Passed" if score >= 75 else "Failed"
print(result)
