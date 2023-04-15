# ------------------------------------------------------------
# -----------------**## Recursive Functions ##**--------------

import sys

# ******------****** Example 21


def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))


num = 2
num = 3
num = 4
num = 5
num = 6

"""
2             ->>>>>>> 1 * 2
3             ->>>>>>> 1 * 2 * 3
4             ->>>>>>> 1 * 2 * 3 * 4
5             ->>>>>>> 1 * 2 * 3 * 4 * 5
6             ->>>>>>> 1 * 2 * 3 * 4 * 5 * 6
"""

# print("The factorial of", num, "is", factorial(num))

print(sys.getrecursionlimit())


# def recursor():
#     recursor()


# recursor()
