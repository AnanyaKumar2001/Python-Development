integer = 33154689

print("Given Number:", integer)

while (integer > 0):
    digit = integer % 10

    integer = integer // 10

    print(digit)
