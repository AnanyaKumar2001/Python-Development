# ------------------------------------------------------------
# ----------------**## How For Loops Work ##**----------------


# --**--**--**--**--** Example 3 ->>>> the workings of a for loop

numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number)


iterable_obj = iter(numbers)

# infinite while loop

while True:
    try:
        # get the next item
        element = next(iterable_obj)

        # do something with the element
        print(f"Element: {element}")

    except StopIteration:
        break
