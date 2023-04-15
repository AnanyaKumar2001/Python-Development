lower_bound = int(input("Enter First Number: "))
upper_bound = int(input("Enter Second Number: "))

if lower_bound < upper_bound:
    print(f"The Prime Numbers Between {lower_bound} & {upper_bound} are:")

    for number in range(lower_bound, upper_bound + 1):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                print(number)


elif lower_bound == upper_bound:
    print("The first and second numbers cannot be equal.")
else:
    print("The first number cannot be greater that the second one.")
