def recur_nat(n):
    if n <= 1:
        return n
    else:
        return n + recur_nat(n - 1)


number = int(input("Enter a Number: "))

if number <= 0:
    print("Please enter a positive integer")
else:
    print("The sum is", recur_nat(number))
