# ------------------------------------------------------------
# --------------------**## Inheritance ##**-------------------


# --**--**--**--**--** Example 34 ->>>> method inheritance

# class John:
#     def sing(self):
#         print("Singing")

#     def run(self):
#         print("Running")


# class Jane:
#     def sing(self):
#         print("Singing")

#     def jog(self):
#         print("Jogging")


# define a parent/base class
# class Person:
#     def sing(self):
#         print("Singing")


# sub/child/derived classes
# class John(Person):
#     def run(self):
#         print("Running")


# class Jane(Person):
#     def jog(self):
#         print("Jogging")


# runner = John()
# runner.sing()

# jogger = Jane()
# jogger.sing()


# --**--**--**--**--** Example 35 ->>>> attribute inheritance
class Person:
    def __init__(self):
        self.employed = True

    def sing(self):
        print("Singing")


class John(Person):
    def run(self):
        print("Running")


class Jane(Person):
    def jog(self):
        print("Jogging")

# runner = John()
# runner.employed

# jogger = Jane()
# jogger.employed
