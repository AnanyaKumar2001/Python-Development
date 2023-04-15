# ------------------------------------------------------------
# -----------------**## The Object Class ##**-----------------


# --**--**--**--**--** Example 36
class Person:
    def __init__(self):
        self.employed = True

    def sing(self):
        print("Singing")


class John(Person):
    def running(self):
        print("Running")


runner = John()


# to find out if an object is an instance of a class
# print(isinstance(runner, John))
# print(isinstance(runner, Person))

# print(isinstance(Person, object))

base_object = object()

# base_object.

# runner.


# to find out if a class inherits from another class
# print(issubclass(John, Person))
print(issubclass(John, object))
