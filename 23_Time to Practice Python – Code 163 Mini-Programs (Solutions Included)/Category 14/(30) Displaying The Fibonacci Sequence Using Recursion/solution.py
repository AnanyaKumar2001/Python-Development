def fibo(n):
    if n <= 1:
        return n
    else:
        result = fibo(n - 1) + fibo(n - 2)

        return result


terms = int(input("Enter Number of Terms: "))

if terms <= 0:
    print("Please entera positive number")
else:
    print("The Fibonacci Sequence:")

    for x in range(terms):
        print(fibo(x))
