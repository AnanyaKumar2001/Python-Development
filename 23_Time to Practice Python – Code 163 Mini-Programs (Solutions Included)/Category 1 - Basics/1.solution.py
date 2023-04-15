def multiplication_or_addition(num1, num2):
    product = num1 * num2

    if product <= 1000:
        return product

    else:
        return num1 + num2


result = multiplication_or_addition(35, 36)
print(result)
