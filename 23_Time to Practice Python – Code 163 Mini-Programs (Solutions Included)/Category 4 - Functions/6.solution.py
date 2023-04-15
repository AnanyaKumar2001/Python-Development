def calculate_sum(num):
    if num:
        return num + calculate_sum(num - 1)
    else:
        return 0


result = calculate_sum(5)
print(result)
