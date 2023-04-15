lower_bound = int(input("Enter First Number: "))
upper_bound = int(input("Enter Second Number: "))

if lower_bound > upper_bound:
    print("The second number cannot be larger that the first one")
elif lower_bound == upper_bound:
    print("Please enter two different numbers")
else:
    for number in range(lower_bound, upper_bound + 1):
        order = len(str(number))
        sum = 0
        temp_value = number

        while temp_value > 0:
            digit = temp_value % 10
            sum += digit ** order
            temp_value //= 10

        if number == sum:
            print(number)
