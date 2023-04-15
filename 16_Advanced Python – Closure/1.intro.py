# ------------------------------------------------------------
# --------------**## Introduction to Closure ##**-------------

# Nested Functions
# nonlocal variables


# --**--**--**--**--** Example 1 ->>>> a nested function

# def person(address):

#     def john():
#         print(address)

#     john()

# person("USA")


# --**--**--**--**--** Example 2 ->>>> nonlocal variable modification

# def outer():
#     number = 85

#     def inner():
#         nonlocal number

#         number = 95

#         print("Inner Function:", number)

#     inner()

#     print("Outer Function:", number)

# outer()


# --**--**--**--**--** Example 3 ->>>> defining a closure

# def person(address):

#     def john():
#         print(address)

#     return john


# john_address = person("USA")
# print(john_address)

# john_address()


# --**--**--**--**--** Example 4 ->>>> deleting the original/enclosing scope


def person(address):

    def john():
        print(address)

    return john


john_address = person("USA")

del person

john_address()
