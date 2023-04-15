number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))

if number1 <= 0 or number2 <= 0:
    print("Entered numbers cannot be zero or less")
else:
    def calculate_HCF(number1, number2):
        if number1 > number2:
            smallest = number2
        else:
            smallest = number1

        for x in range(1, smallest + 1):
            if (number1 % x == 0) and (number2 % x == 0):
                HCF_number = x

        return HCF_number

    print("The HCF is:", calculate_HCF(number1, number2))
