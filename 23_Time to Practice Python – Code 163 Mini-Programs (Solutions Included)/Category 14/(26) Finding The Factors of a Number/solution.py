number = int(input("Enter a Number: "))

if number <= 0:
    print("Please enter a positive integer")
else:
    def factors(num):
        print(f"The factors of {num} are:")

        for x in range(1, num + 1):
            if num % x == 0:
                print(x)

    factors(number)
