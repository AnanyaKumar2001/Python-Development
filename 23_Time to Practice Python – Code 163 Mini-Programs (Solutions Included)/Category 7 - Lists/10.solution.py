list = [5, 20, 15, 20, 25, 50, 20]


def remove_value(sample_list, val):
    return [value for value in sample_list if value != val]


result_list = remove_value(list, 20)
print(result_list)
