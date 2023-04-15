# ------------------------------------------------------------
# ----------------**## Namespace Part 1 ##**------------------

# *****************---------------- Example
number = 1001

# print(id(number))
# print(id(1001))

# *****************---------------- Example

a = 2
print("a:", id(a))

a = a + 1
print("a1:", id(a))
print("Three:", id(3))

b = 2
print("b:", id(b))
print("Two:", id(2))

# *****************---------------- Example

something = 12
something = "Jack"
something = ["a", 2, True]

# *****************---------------- Example


def hello():
    print("Hello World")


something = hello
something()
