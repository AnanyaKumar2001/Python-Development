
number = int(input("Enter a Number: "))
# number = 9474


# finding the order of the number
order = len(str(number))
# print(order)
# print(type(order))

sum = 0

temp_value = number

while temp_value > 0:
    digit = temp_value % 10
    # first value of digit => 3
    # second value of digit => 6
    # third value of digit => 6

    # sum = sum + digit ** order
    sum += digit ** order
    # first value of sum => 0 + 3 ** 3 =>> 0 + 27 = 27
    # second value of sum => 27 + 6 ** 3 =>>> 27 + 216 = 243
    # third value of sum => 243 + 6 ** 3 =>>>> 216 + 243 = 459

    # temp_value = temp_value // 10
    temp_value //= 10
    # original value of temp_value =>>> 663
    # first value of temp_value =>>> 66
    # second value of temp_value =>>> 6

if number == sum:
    print("an Armstrong Number")
else:
    print("NOT an Armstrong Number")
