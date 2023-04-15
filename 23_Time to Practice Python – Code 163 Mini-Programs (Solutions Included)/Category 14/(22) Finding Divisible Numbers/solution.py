divisor = int(input("Enter a Divisor: "))

dividend_lower_limit = int(input("Enter a Dividend Lower Limit: "))
dividend_upper_limit = int(input("Enter a Dividend Upper Limit: "))

if dividend_lower_limit > dividend_upper_limit:
    print("The lower limit cannot be less than the upper limit")
elif dividend_lower_limit == dividend_upper_limit:
    print("The dividend limits cannot be equal")
elif dividend_upper_limit < divisor:
    print("The divisor cannot be larger that the upper limit")
elif divisor <= 0:
    print("The divisor cannot be zero or less")
else:
    numbers_range = [x for x in range(
        dividend_lower_limit, dividend_upper_limit + 1)]

    # print(numbers_range)

    result = list(filter(lambda y: (y % divisor == 0), numbers_range))

    print(f"Numbers divisible by {divisor} are:")

    for z in result:
        print(z)
