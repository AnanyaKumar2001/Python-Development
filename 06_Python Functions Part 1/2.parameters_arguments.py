# ------------------------------------------------------------
# ---------**## Function Parameters & Arguments ##**----------


# ***************------------ Example 4

def arithmetic_operations(x, y):
    print(f"{x} * {y} = {x * y}")
    print(f"{x} / {y} = {x / y}")
    print(f"{x} + {y} = {x + y}")
    print(f"{x} - {y} = {x - y}")

# arithmetic_operations(20, 5)
# arithmetic_operations(112, 32)
# arithmetic_operations(301, 201)

# ***************------------ Example 5


def legal_age(name, age, allowed_age):
    if age >= allowed_age:
        print(f"{name} is allowed to drive.")
    else:
        print(f"{name} is NOT allowed to drive.")


legal_age("Tom", 21, 18)
legal_age("Sarah", 17, 18)
legal_age("John", 18, 21)
