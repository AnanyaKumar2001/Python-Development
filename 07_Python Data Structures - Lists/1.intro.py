# ------------------------------------------------------------
# ----------------**## Lists Introduction ##**----------------


# ******------****** Example 1 ->>>> a simple list

numbers = [1, 2, 64, 124, 654]
names = ["John", "Mark", "Emily", "Sandra"]
# print(names)


# ******------****** Example 2 ->>>> a list of lists

likes = [["tv", "gmaing"], ["pizza", "pasta"]]
# print(likes)


# ******------****** Example 3 ->>>> a list of lists of lists

mixed = [[1, True], "Cat", "Dog", [["wind", "water"], ["earth", "fire"]]]
# print(mixed)

# ******------****** Example 4 ->>>> a list of identical items
animal = ["cat"] * 10
# print(animal)


# ******------****** Example 5 ->>>> list merging/concatenation

even_nums = [2, 4, 6, 8, 10]
odd_nums = [1, 3, 5, 7, 9]
cities = ["Kabul", "New York", "London"]
boolean = [True, False]

mixed_data = even_nums + odd_nums + cities + boolean

print(mixed_data)
