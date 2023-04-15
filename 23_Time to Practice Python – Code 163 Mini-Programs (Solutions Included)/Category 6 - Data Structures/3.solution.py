sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

element_count = dict()

for item in sample_list:
    if item in element_count:
        element_count[item] += 1
    else:
        element_count[item] = 1

print(element_count)
