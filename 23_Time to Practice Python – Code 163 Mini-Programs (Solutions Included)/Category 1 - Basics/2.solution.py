def sum_num(num):
    previous_num = 0

    for number in range(num):
        sum = previous_num + number

        print("Current Num:", number, "Previous Num:", previous_num, "Sum:", sum)

        previous_num = number


sum_num(10)
