# ------------------------------------------------------------
# ----------**## Non-keyword Arguments (*args) ##**-----------


# ***************------------ Example 9

def sum(x, y):
    return x + y

# print(sum(89, 98))
# print(sum(89, 98, 23, 56, 45))

# ***************------------ Example 10


def num(*numbers):
    return numbers

# print(num(10, 21, 65, 112, 555, 666))

# ***************------------ Example 11


def subtract(*nums):
    number = 100
    for x in nums:
        number = number - x
    return number


print(subtract(2, 3, 5, 25, -45, 111))
