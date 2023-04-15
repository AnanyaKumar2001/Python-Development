# ------------------------------------------------------------
# --------------------**## Zip Functions ##**-----------------


# ******------****** Example 9
numbers_list = [1, 2, 3]
names_list = ['Adrianna', 'Cecile', 'Darcey']

# No iterables are passed
# result = zip()

# converting the iterator to a list
# result_list = list(result)
# print(result_list)

# two iterables are passed
# result = zip(numbers_list, names_list)

# converting the iterator to a set
# result_set = set(result)
# print(result_set)

# ******------****** Example 10 ->>>> different number of iterables

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names_list = ['Adrianna', 'Cecile', 'Darcey']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR', "FIVE", "SIX")

# result = zip(numbers_list, numbers_tuple)

# converting to set
# result_set = set(result)
# print(result_set)

# result = zip(numbers_list, names_list, numbers_tuple)

# converting to a list
# result_list = list(result)
# print(result_list)


# ******------****** Example 11 ->>>> unzipping the values using the zip()

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

unzipped_coordinates, unzipped_values = zip(*result_list)

# unzipped iterables are converted to a tuple
print("Unzipped Coordinates:", unzipped_coordinates)
print("Unzipped Values:", unzipped_values)
