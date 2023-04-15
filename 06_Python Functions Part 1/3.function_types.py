# ------------------------------------------------------------
# ----------------**## Function Types ##**--------------------

# 1- Functions that perform a task
# 2- Functions that calculate and return a value

# ***************------------ Example 6

def facebook(name, status):
    return f"{name} is {status}"


user1_status = facebook("William", "offline")
user2_status = facebook("Tiffany", "online")
# print(user1_status)
# print(user2_status)


# ***************------------ Example 7
# Keyword Arguments

def multiply(number, by):
    return number * by


# result = multiply(15, 4)
# print(result)

# print(multiply(2.3, 1.2))

result = multiply(number=65, by=15)
print(result)
