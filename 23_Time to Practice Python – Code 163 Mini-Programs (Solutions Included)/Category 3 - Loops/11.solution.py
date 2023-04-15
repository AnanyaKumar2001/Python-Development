start = 1
end = 50

print(f"Prime Number between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                break

        else:
            print(num)
