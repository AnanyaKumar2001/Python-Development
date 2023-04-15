# ------------------------------------------------------------
# ----------**## Required & Optional Parameters ##**----------


# ***************------------ Example 8

def working_condition(device, status="working"):
    return f"The {device} is {status}"

# print(working_condition("Drill Press"))
# print(working_condition("Welding Maching", "out of order"))


# ***************------------ Example 9

def subtract(x, z, y=15):
    return x - y - z


print(subtract(20, 5))
print(subtract(20, 5, 10))
