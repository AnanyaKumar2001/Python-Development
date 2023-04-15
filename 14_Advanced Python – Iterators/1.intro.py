# ------------------------------------------------------------
# ------------**## Introduction to Iterators ##**-------------


# --**--**--**--**--** Example 1 ->>>> __iter__() & __next__()
numbers = [1, 2, 3, 4, 5]


first_iterator = iter(numbers)

print(next(first_iterator))
print(next(first_iterator))

# next() == __next__()

print(first_iterator.__next__())
print(first_iterator.__next__())
print(type(first_iterator.__next__()))
# print(first_iterator.__next__())


# --**--**--**--**--** Example 2 ->>>> using a for loop

for number in numbers:
    print(number)
