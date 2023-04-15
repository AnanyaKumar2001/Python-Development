num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if (num1 > num2) and (num1 > num3):
    num_largest = num1
elif (num2 > num1) and (num2 > num3):
    num_largest = num2
else:
    num_largest = num3

if num_largest == num1 and num_largest == num2 and num_largest == num3:
    print("The input numbers are the same. Please enter different numbers")
else:
    print("The Largest Number is:", num_largest)
