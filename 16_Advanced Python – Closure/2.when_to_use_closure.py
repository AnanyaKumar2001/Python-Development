# ------------------------------------------------------------
# ----------------**## When to use Closure ##**---------------


# --**--**--**--**--** Example 5

def numbers(n):

    def multiply_by(x):
        return x * n

    return multiply_by


three = numbers(3)
four = numbers(4)
five = numbers(5)
string = numbers("Muslim")

# print(three)
# print(type(three))

# print(three(30))
# print(four(40))
# print(five(50))

# print(numbers.__closure__)


# print(three.__closure__)
# print()
# print(string.__closure__)

print(three.__closure__[0].cell_contents)

print(four.__closure__[0].cell_contents)

print(five.__closure__[0].cell_contents)

print(string.__closure__[0].cell_contents)
