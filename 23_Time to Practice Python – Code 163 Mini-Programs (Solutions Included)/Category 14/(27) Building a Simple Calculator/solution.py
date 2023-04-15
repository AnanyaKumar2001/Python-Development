# Adding two numbers
def addition(num1, num2):
    return num1 + num2


# Sutracting two numbers
def subtraction(num1, num2):
    return num1 - num2


# Multiplying two numbers
def multiplication(num1, num2):
    return num1 * num2


# Dividding two numbers
def division(num1, num2):
    return num1 / num2


print("Please Select an Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multipllication")
print("4. Division")
print()

while True:
    input_num = int(input("Enter Your Choice (1/2/3/4): "))

    if input_num in (1, 2, 3, 4):
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))

        if input_num == 1:
            print(f"{num1} + {num2} = {addition(num1, num2)}")

        elif input_num == 2:
            print(f"{num1} - {num2} = {subtraction(num1, num2)}")

        elif input_num == 3:
            print(f"{num1} x {num2} = {multiplication(num1, num2)}")

        elif input_num == 4:

            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print(f"{num1} / {num2} = {round(division(num1, num2), 2)}")

        break

    else:
        print("Invalid Operation")
