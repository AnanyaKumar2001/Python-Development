# ------------------------------------------------------------
# ---------------**## Chaining Decorators ##**----------------


# --**--**--**--**--** Example 10

def info_name(func):

    def full_name(*args):

        func(*args)

    return full_name


def info_last_name(func):

    def full_name(*args):

        func(*args)

    return full_name


@info_name
@info_last_name
def info(name, lastname):
    print(f"My Full Name is {name} {lastname}")


info("Muslim", "Helalee")
