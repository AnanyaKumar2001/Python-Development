# 0 1 1 2 3 5 8 13 21 34 55 89

terms = int(input("Enter Number of Terms: "))

x1, x2 = 0, 1
count = 0

if terms <= 0:
    print("Please enter a positive integer")
elif terms == 1:
    print(f"The first term of the Fibonacci Sequence is: ")
    print(x1)
else:
    print("The fibonacci Sequence is: ")

    while count < terms:
        print(x1)

        nth = x1 + x2

        # updating the values
        x1 = x2
        x2 = nth
        count += 1
"""
First---------
>>>> x1 = 0 ->>>> shown on the screen
nth = 0 + 1
x1 = 1
x2 = 1

Second--------
>>>> x1 = 1
nth = 1 + 1
x1 = 1
x2 = 2

Third---------
>>>>> x1 = 1
nth = 1 + 2
x1 = 2
x2 = 3

Forth------
>>>>> x1 = 2
nth = 2 + 3
x1 = 3
x2 = 5

Fifth------
>>>>> x1 = 3
nth = 3 + 5
x1 = 5
x2 = 8


"""
