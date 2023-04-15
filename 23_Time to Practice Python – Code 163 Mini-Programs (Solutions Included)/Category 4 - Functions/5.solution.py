def outer_func(a, b):

    def inner_func(a, b):
        return a + b

    add = inner_func(a, b)

    return add + 5


result = outer_func(5, 10)
print(result)
