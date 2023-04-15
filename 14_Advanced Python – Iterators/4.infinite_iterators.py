# ------------------------------------------------------------
# ----------------**## Infinite Iterators ##**----------------


# --**--**--**--**--** Example 6 ->>>> infinite iterators using the next() method

# print(int())

# number = iter(int, 1)
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))


# --**--**--**--**--** Example 7 ->>>> infinite iterators using for loops

# for element in number:
#     print(element)

# --**--**--**--**--** Example 8 ->>>> infinite iterators using classes

class OddNums:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num


odd_nums = OddNums()

iterable_nums = iter(odd_nums)

print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
print(next(iterable_nums))
