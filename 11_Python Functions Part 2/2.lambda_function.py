# ------------------------------------------------------------
# ------------**## Anonymous / Lambda Function ##**-----------


# ******------****** Example 3

products = [
    ("Product-1", 15),
    ("Product-2", 25),
    ("Product-3", 5),
    ("Product-4", 45),
    ("Product-5", 20),
    ("Product-6", 30),
]

products.sort(key=lambda product: product[1])
# print(products)

# ******------****** Example 4 ->>>> lambda + filter()

my_list = [1, 5, 4, 6, 8, 11, 3, 12, 34, 55]

# new_list = filter(lambda x: (x % 2 == 0), my_list)

# print(new_list)

# for num in new_list:
#     print(num)


# even_nums = list(new_list)
# print(even_nums)


# ******------****** Example 5 ->>>> lambda + map()
new_list = list(map(lambda x: x * 2, my_list))
print(new_list)
