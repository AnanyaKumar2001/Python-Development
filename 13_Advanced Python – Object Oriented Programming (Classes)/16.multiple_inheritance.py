# ------------------------------------------------------------
# ---------------**## Multiple Inheritance ##**---------------


# --**--**--**--**--** Example 39 ->>>> Bad Multiple Inheritance
# class Person:
#     def sport_status(self):
#         print("Runner")


# class John:
#     def sport_status(self):
#         print("Jogger")


# class Jane(Person, John):
#     pass


# class Jane(John, Person):
#     pass


# jane = Jane()
# jane.sport_status()


# --**--**--**--**--** Example 40 ->>>> Good Multiple Inheritance
class Person:
    def runner(self):
        print("Runner")


class John:
    def jogger(self):
        print("Jogger")


class Jane(Person, John):
    pass


jane = Jane()
jane.runner()
jane.jogger()
