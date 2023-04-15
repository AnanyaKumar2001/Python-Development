# ------------------------------------------------------------
# -------**## Decorating Functions with Parameters ##**-------


# --**--**--**--**--** Example 6 ->>>> function with parameters

# def operation(x, y):
#   return x / y

# print(operation(10, 20))
# print(operation(101, 32))
# print(operation(54, 0))


# to use a decorator

def operation(func):

    def inner(x, y):
        print(f"{x} / {y} =")

        if y == 0:
            print("cannot divide by zero")
            return

        return func(x, y)

    return inner


@operation
def divide(x, y):
    print(x / y)


divide(2, 5)
print()
divide(20, 5)
print()
divide(78, 0)
