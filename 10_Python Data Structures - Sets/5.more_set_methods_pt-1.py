# ------------------------------------------------------------
# --------------**## More Set Methods Part 1 ##**-------------


# ******------****** Example 23 ->>>> copy()
numbers = {101, 202, 303, 404, 505, 606}
other_numbers = numbers
# print(numbers)
# print(other_numbers)

# numbers.remove(606)
# print(numbers)
# print(other_numbers)

# other_numbers.discard(505)
# print(numbers)
# print(other_numbers)

some_numbers = numbers.copy()
# print(numbers)
# print(some_numbers)


some_numbers.add(909)
# print(numbers)
# print(some_numbers)

# print(id(numbers))
# print(id(some_numbers))
# print(id(other_numbers))


# ******------****** Example 24 ->>>> isdisjoint() with sets
# A = {1, 2, 3, 4}
# B = {5, 6, 7}
# C = {4, 5, 6}
# D = {10, 20, 30, 7}

# print('Are A and B disjoint?', A.isdisjoint(B))  # True
# print('Are A and C disjoint?', A.isdisjoint(C))  # False
# print('Are B and C disjoint?', B.isdisjoint(C))  # False
# print('Are A and D disjoint?', A.isdisjoint(D))  # True
# print('Are B and D disjoint?', B.isdisjoint(D))  # False
# print('Are C and D disjoint?', C.isdisjoint(D))  # True


# ******------****** Example 25 ->>>> isdisjoint() with other iterables

A = {'a', 'b', 'c', 'd'}
B = ['b', 'e', 'f']
C = '5de4'
D = {1: 'a', 2: 'b'}
E = {'a': 1, 'b': 2}
F = ("z", "g", "s")

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))
print('Are A and D disjoint?', A.isdisjoint(D))
print('Are A and E disjoint?', A.isdisjoint(E))
print('Are A and F disjoint?', A.isdisjoint(F))
