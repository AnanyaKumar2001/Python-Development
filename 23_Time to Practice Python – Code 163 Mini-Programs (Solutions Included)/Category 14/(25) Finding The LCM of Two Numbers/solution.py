num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if (num1 <= 0) or (num2 <= 0):
    print("Entered numbers cannot be zero or less")
else:
    def calculate_LCM(number1, number2):
        if number1 > number2:
            greater = number1
        else:
            greater = number2

        while greater:
            if (greater % number1 == 0) and (greater % number2 == 0):
                LCM_number = greater
                break
            greater += 1

        return LCM_number

    print("The LCM is:", calculate_LCM(num1, num2))
