number = int(input("Enter a Number: "))

if number > 1:
    for x in range(2, number):
        if number % x == 0:
            print(number, "is not is prime number")
            print(x, "times", round(number/x), "is", number)
            break
    else:
        print(number, "is a prime number")

else:
    print(number, "is not a prime number")
