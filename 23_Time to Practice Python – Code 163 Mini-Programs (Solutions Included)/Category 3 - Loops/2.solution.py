print("THe Pattern is as follows")

last_num = 40

for row in range(1, last_num):
    for column in range(1, row + 1):
        print(column, end=" ")
    print("")
