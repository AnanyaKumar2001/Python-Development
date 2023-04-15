# ------------------------------------------------------------
# -------------------**## Magic Methods ##**------------------

# Magic Methods Reference
# https://rszalski.github.io/magicmethods/


# --**--**--**--**--** Example 11 ->>>> __str__ magic method

# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def walk(self):
#         print(f"Walking Coordinates ({self.x}, {self.y})")


# test = Robot(0.1, 0.5)
# print(test)


# --**--**--**--**--** Example 12 ->>>> converting to a string


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"I am a magic method with coordinates ({self.x}, {self.y})"

    def walk(self):
        print(f"Walking Coordinates ({self.x}, {self.y})")


test = Robot(0.1, 0.5)
# print(test)


print(str(test))
