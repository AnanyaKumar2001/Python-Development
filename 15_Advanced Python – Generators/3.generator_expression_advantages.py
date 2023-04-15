# ------------------------------------------------------------
# ---------**## Generator Expressions Advantages ##**---------

# -*-*-*-*-*-*-*-*-*-* 1- Memory Efficient --------------------
# -*-*-*-*-*-*-*-*-*-* 2- Ease of Implementation --------------
# -*-*-*-*-*-*-*-*-*-* 3- Representing Infinite Stream --------
# -*-*-*-*-*-*-*-*-*-* 4- Pipelining Generators --------------


# --**--**--**--**--** Example 5 ->>>> Ease of Implementation
# def number_power(maxi_num):
#     n = 0
#     while n <= maxi_num:
#         yield 2 ** n
#         n += 1

# result = number_power(2)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

# --**--**--**--**--** Example 6 ->>>> Representing Infinite Stream

# def even_nums():
#     n = 0
#     while True:
#         yield n

#         n += 2

# all_even = even_nums()
# print(next(all_even))
# print(next(all_even))
# print(next(all_even))
# print(next(all_even))
# print(next(all_even))
# print(next(all_even))
# print(next(all_even))
# print(next(all_even))
# print(next(all_even))


# --**--**--**--**--** Example 7 ->>>> Pipelining Generators

# Fib Num Series ->>> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ....

def fibonacci_numbers(nums):
    x, y = 0, 1

    for _ in range(nums):
        x, y = y, x+y

        yield x


fib_nums = fibonacci_numbers(10)
# print(next(fib_nums))
# print(next(fib_nums))
# print(next(fib_nums))
# print(next(fib_nums))
# print(next(fib_nums))
# print(next(fib_nums))
# print(next(fib_nums))
# print(next(fib_nums))
# print(next(fib_nums))
# print(next(fib_nums))
# print(next(fib_nums))


def square(nums):
    for num in nums:
        yield num ** 2


sqrt_nums = square(fibonacci_numbers(10))
# print(next(sqrt_nums))
# print(next(sqrt_nums))
# print(next(sqrt_nums))
# print(next(sqrt_nums))
# print(next(sqrt_nums))
# print(next(sqrt_nums))
# print(next(sqrt_nums))
# print(next(sqrt_nums))

print(sum(square(fibonacci_numbers(10))))
