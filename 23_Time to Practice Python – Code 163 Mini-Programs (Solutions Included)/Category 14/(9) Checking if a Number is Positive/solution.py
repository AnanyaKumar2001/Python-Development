# Approach One ->>>> using if...elif...else

# number = int(input("Enter a Number: "))

# if number > 0:
#     print("you have entered a positive number")
# elif number == 0:
#     print("you have entered zero")
# else:
#     print("you have entered a negative number")

# ----------------------------------------------------------------
def input_number():
    number = int(input("Enter a Number: "))

    if number > 0:
        print("you have entered a positive number")
    elif number == 0:
        print("you have entered zero")
    else:
        print("you have entered a negative number")


try:
    input_number()
except:
    print("Please Enter a Valid Number")

# ----------------------------------------------------------------

# Approach Two ->>>> using nested conditionals
# if number >= 0:
#     if number > 0:
#         print("you have entered a positive number")
#     else:
#         print("you have entered zero")
# else:
#     print("you have entered a negative number")
