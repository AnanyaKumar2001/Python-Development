list_one = [3, 6, 9, 12, 15, 18, 21]
list_two = [4, 8, 12, 16, 20, 24, 28]

list_three = list()

odd_elements = list_one[1::2]
print(odd_elements)

even_elements = list_two[0::2]
print(even_elements)


list_three.extend(odd_elements)
list_three.extend(even_elements)
print(list_three)
