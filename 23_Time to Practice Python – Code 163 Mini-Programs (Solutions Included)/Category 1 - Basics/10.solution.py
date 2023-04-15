def merge_list(list_one, list_two):
    list_three = []

    for num in list_one:
        if (num % 2 != 0):
            list_three.append(num)

    for num in list_two:
        if (num % 2 == 0):
            list_three.append(num)

    return list_three


list1 = [10, 20, 23, 11, 17, 44, 55]
list2 = [13, 43, 24, 36, 12, 33, 66]

print(merge_list(list1, list2))
