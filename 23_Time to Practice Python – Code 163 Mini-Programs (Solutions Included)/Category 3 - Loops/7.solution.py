num1 = 5
num2 = 5

for i in range(0, num1 + 1):
    for j in range(num2 - i, 0, -1):
        print(j, end=" ")
    print()
