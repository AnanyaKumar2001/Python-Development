# ------------------------------------------------------------
# ---------------**## Conditional Statements ##**-------------

"""
if (boolean expression):
  execute the statements

"""

# ****************------------- Example ->>> Check for a single condition
# temperature = 35
# temperature = 29
# temperature = 24
# temperature = -10
# temperature = 35
# temperature = 45
# temperature = 55

# if temperature > 30:
#     print("It is a good day for walking")


# print("It is not part of the if statement")

# ****************------------- Example ->>> Check for 2 conditions

# if temperature > 25:
#     print("Awesome")
# else:
#     print("Cold")

# ****************------------- Example ->>> Check for mul
# temperature = 55
# temperature = 35
# temperature = 34
# temperature = 25
# temperature = 24
# temperature = 20
temperature = 19
temperature = -10


if temperature >= 35:
    print("Hot")
elif temperature > 25:
    print("Awesome")
elif temperature < 20:
    print("Cold")
else:
    print("Undecided")
