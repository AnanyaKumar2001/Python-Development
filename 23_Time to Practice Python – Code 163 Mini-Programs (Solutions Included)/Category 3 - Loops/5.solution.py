list = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for item in list:
    if (item > 100):
        break

    if (item % 5 == 0):
        print(item)
