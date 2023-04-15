# ------------------------------------------------------------
# ----------------**## Namespace Part 2 ##**------------------


# *************------------- Example

def outer():
    outer_number = 100
    # print(id(outer_number))

    global global_number
    global_number = 101
    print("Global number =", global_number)

    def inner():
        inner_number = 200
        inner_number = "Jack"
        # print("Inner number =", inner_number)

        outer_number = 500
        # print(id(outer_number))
        # print("Outer number =", outer_number)

    inner()


global_number = 300
print(global_number)


outer()

print(global_number)
