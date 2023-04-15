# ------------------------------------------------------------
# -------------**## Building Custom Iterators ##**------------


# --**--**--**--**--** Example 4 ->>>> building a custom iterator
class NumberPower:
    def __init__(self, maxi_num):
        self.maxi_num = maxi_num

    # creating the iterator object
    def __iter__(self):
        self.n = 0
        return self

    # iterate over the created iterator object and generate one value each time
    def __next__(self):
        if self.n <= self.maxi_num:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# creating an instance/object of the class NumberPower
num_pow = NumberPower(2)


# creating an iterable from the object
iterable_data = iter(num_pow)

# using the next() to go to the next iterator element
# print(next(iterable_data))
# print(next(iterable_data))
# print(next(iterable_data))
# print(next(iterable_data))


# --**--**--**--**--** Example 5 ->>>> iterating using a for loop

for i in NumberPower(2):
    print(i)
