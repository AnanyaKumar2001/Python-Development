# ------------------------------------------------------------
# --------------------**## Map Functions ##**-----------------


# ******------****** Example 6 ->>>> working of map()

# Iterable
# numbers = (1, 2, 3, 4, 5)

# Function


# def calculate_square(n):
#     return n * n


# result = map(calculate_square, numbers)
# print(result)

# Converting a map object to a set
# num_square = set(result)
# print(num_square)


# Converting a map object to a tuple
# num_square = tuple(result)
# print(num_square)

# Converting a map object to a list
# num_square = list(result)
# print(num_square)


# ******------****** Example 7 ->>>> lambda + map()
# numbers = (1, 2, 3, 4, 5)
# letters = ["a", "b", "c"]

# result = map(lambda x: x, letters)
# result = map(lambda x: (x * x) / 2, numbers)
# print(result)

# Converting a map object to a set
# character = set(result)
# print(character)


# Converting a map object to a tuple
# character = tuple(result)
# print(character)

# Converting a map object to a list
# character = list(result)
# print(character)


# ******------****** Example 8 ->>>> passing multiple iterables to the map method

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [7, 8]

result = map(lambda n1, n2: n1 + n2, numbers1, numbers2)
# print(tuple(result))
# print(set(result))
