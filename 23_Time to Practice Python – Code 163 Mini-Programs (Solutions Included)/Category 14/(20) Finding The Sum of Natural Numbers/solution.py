number = int(input("Enter a Number: "))

if number < 0:
    print("Please enter a positive integer")
else:
    sum = 0

    while number > 0:
        sum += number

        number -= 1

    print("The sum of the natural numbers is equal to:", sum)
