# ------------------------------------------------------------
# ------------------**## For Loops Part 2 ##**----------------


# ****************----------------- Example 6

# status = True

# for number in range(1, 4):
#     print(f"Attempt {number}")

#     if status:
#         print("Success")
#         break


# ****************----------------- Example 7


status = False

for number in range(1, 4):
    print(f"Attempt {number}")

    if status:
        print("Success")
        break
else:
    print("Failed")
