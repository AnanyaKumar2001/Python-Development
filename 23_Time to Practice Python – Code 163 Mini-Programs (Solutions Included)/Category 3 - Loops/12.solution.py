num = 7654321

reversed_num = 0

while num > 0:
    remainder = num % 10

    reversed_num = (reversed_num * 10) + remainder

    num = num // 10

print("Reversed Number:", reversed_num)
