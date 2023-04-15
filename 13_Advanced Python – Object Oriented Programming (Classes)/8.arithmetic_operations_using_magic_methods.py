# ------------------------------------------------------------
# -----**## Arithmetic Operations Using Magic Methods ##**----


# --**--**--**--**--** Example 17 ->>>> __add__ magic method
# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return f"Coordinates({self.x + other.x}, {self.y + other.y})"


# test = Robot(12, 1)
# other_test = Robot(4.12, 8.45)

# print(test.x)
# print(test.y)
# print(other_test.x)
# print(other_test.y)

# print(test + other_test)


# --**--**--**--**--** Example 18 ->>>> __sub__ magic method

# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __sub__(self, other):
#         return f"Coordinates({self.x - other.x}, {self.y - other.y})"


# test = Robot(12, 11)
# other_test = Robot(4.12, 8)
# print(test - other_test)


# --**--**--**--**--** Example 19 ->>>> __mul__ magic method
# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __mul__(self, other):
#         return f"Coordinates({self.x * other.x}, {self.y * other.y})"


# test = Robot(12, 11)
# other_test = Robot(4.12, 8)
# print(test * other_test)


# --**--**--**--**--** Example 20 ->>>> __floordiv__ magic method

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __floordiv__(self, other):
        return f"Coordinates({self.x // other.x}, {self.y // other.y})"


test = Robot(10, 20)
other_test = Robot(2, 3)
print(test // other_test)
