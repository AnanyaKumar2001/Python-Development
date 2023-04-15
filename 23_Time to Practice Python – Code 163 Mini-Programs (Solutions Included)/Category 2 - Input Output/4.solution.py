float_nums = []

list_size = int(input("Enter the list size "))

for i in range(0, list_size):
    print("Enter number at location", i, ":")

    item = float(input())
    float_nums.append(item)

print("The user list is:", float_nums)
