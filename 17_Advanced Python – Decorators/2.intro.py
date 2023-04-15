# ------------------------------------------------------------
# ------------**## Introduction to Decorators ##**------------

# __call__() ->>>> callable


# --**--**--**--**--** Example 4 ->>>> a decorator

# decorator
# def operation(func):

#     def increment():
#         print("before the func")

#         # the execution of the decrement function
#         func()

#         print("after the func")

#     return increment


# decorated
# def decrement():
#     print("The number has been decremented")

# decrement()
# operation(decrement)

# decorated_function = operation(decrement)
# decorated_function()


# --**--**--**--**--** Example 5 ->>>> the syntactic sugar of a decorator
def operation(func):

    def increment():
        print("before the func")

        # the execution of the decrement function
        func()

        print("after the func")

    return increment


@operation
def decrement():
    print("The number has been decremented")


decrement()


# @operation == decrement = operation(decrement)
