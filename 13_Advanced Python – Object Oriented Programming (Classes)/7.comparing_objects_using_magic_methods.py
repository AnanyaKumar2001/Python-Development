# ------------------------------------------------------------
# -------**## Comparing Objects Using Magic Methods ##**------


# --**--**--**--**--** Example 13 ->>>> comparing objects
# class Robot:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

# test = Robot(4.015, 9.2345)
# other_test = Robot(4.015, 9.2345)

# print(test == other_test)

# print(id(test))
# print(id(other_test))


# --**--**--**--**--** Example 14 ->>>> __eq__ magic method
# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#       return self.x == other.x and self.y == other.y


# test = Robot(4.015, 9.2345)
# other_test = Robot(4.015, 9.2345)

# print(test == other_test)


# --**--**--**--**--** Example 15 ->>>> __gt__ magic method

# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y


# test = Robot(15, 35)
# other_test = Robot(4.015, 9.2345)

# print(test > other_test)
# print(test == other_test)
# print(test < other_test)


# --**--**--**--**--** Example 16 ->>>> __lt__ magic method

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y


test = Robot(1, 2)
other_test = Robot(4.015, 9.2345)

# print(test > other_test)
# print(test == other_test)
print(test < other_test)
