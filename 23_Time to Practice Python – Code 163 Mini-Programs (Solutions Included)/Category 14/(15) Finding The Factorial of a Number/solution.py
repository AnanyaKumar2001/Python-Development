number = int(input("Enter a Number: "))

factorial = 1

if number < 0:
    print("Please enter a positive number")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    for x in range(1, number + 1):
        factorial *= x
    print(f"The factorial of {number} is {factorial}")
