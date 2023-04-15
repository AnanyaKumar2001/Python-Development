number = int(input("Enter a Number: "))
numbers = int(input("Enter Number of Terms: "))

result = list(map(lambda x: number ** x, range(numbers)))

print(f"The total terms are: ")

for y in range(numbers):
    print(f"{number} raised to the power of {y} is {result[y]}")
