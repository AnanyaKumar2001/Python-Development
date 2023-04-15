# ------------------------------------------------------------
# ------------------**## Debugging Code ##**------------------


# ***************------------ Example 18

def subtract(*nums):
    target_num = 1000

    for x in nums:
        target_num -= x

    return target_num


print(subtract(50, 32, 91, 24, 7, 123, 306, 68))
