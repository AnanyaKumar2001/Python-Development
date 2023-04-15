def divisible_by_5(num_list):
    print("Given List", num_list)

    for num in num_list:
        if (num % 5 == 0):
            print("Divisible by 5:", num)


list = [10, 20, 33, 46, 55, 77, 105, 204, 335]
divisible_by_5(list)
