# ------------------------------------------------------------
# ------------**## Introduction to Generators ##**------------

# __iter__() & __next__() & iter() are implemented automatically


"""
Normal function *-*-*-*-*-*-*-*-*-*-*-
1- return
2- after the return, the variables are garbage collected
3- return terminates a function
4- performs a task or calculates a value




Gen function *-*-*-*-*-*-*-*-*-*-*-
1- yield
2- access to variables after function yields
3- yield does not terminate a function
4- returns an iterator object

"""


# --**--**--**--**--** Example 1 ->>>> creating a generator

def first_generator():
    x = 1
    print("1st iteration")

    yield x

    x += 1.1
    print("2nd iteration")

    yield x

    x += 1.2
    print("3rd iteration")

    yield x


# my_gen = first_generator()
# print(my_gen)
# print(type(my_gen))

# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))


# --**--**--**--**--** Example 2 ->>>> using a for loop
for element in first_generator():
    print(element)
