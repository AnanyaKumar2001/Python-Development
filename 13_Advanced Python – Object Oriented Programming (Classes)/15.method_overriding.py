# ------------------------------------------------------------
# -----------------**## Method Overriding ##**----------------


# --**--**--**--**--** Example 37 ->>>> overriding
# class Person:
#     def __init__(self):
#         self.employed = True

#     def sing(self):
#         print("Singing")


# class John(Person):
#   # method overriding
#     def __init__(self):
#         self.jogger = True

#     def run(self):
#         print("Running")


# runner = John()

# print(runner.jogger)
# print(runner.employed)


# --**--**--**--**--** Example 38 ->>>> fixing overriding


class Person:
    def __init__(self):
        print("Base Class")
        self.employed = False

    def sing(self):
        print("Singing")


class John(Person):
    def __init__(self):
        # super().__init__()

        print("Sub Class")

        self.jogger = True

        super().__init__()

    def run(self):
        print("Running")


runner = John()

# print(runner.jogger)
# print(runner.employed)
