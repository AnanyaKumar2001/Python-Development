# ------------------------------------------------------------
# -----**## Instance Attributes VS Class Attributes ##**------

# 1- Instance Attr ->>> within the constructor
# 2- Class Attr ->>>> within the class itself


# --**--**--**--**--** Example 6 ->>>> Instance attr
# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def walk(self):
#         print(f"walking coordinates ({self.x}, {self.y})")


# 1st instantiation
# test_walk1 = Robot(8.9, 99.7)
# test_walk1.walk()

# print(test_walk1.x)
# print(test_walk1.y)

# 2nd instantiation
# test_walk2 = Robot(4.5, 6.7)
# test_walk2.walk()

# print(test_walk2.x)
# print(test_walk2.y)


# --**--**--**--**--** Example 7 ->>>> different Instance attr

# test_walk1.z = 2.3
# print(test_walk1.z)

# print(test_walk2.z) # AttributeError

# --**--**--**--**--** Example 8 ->>>> class attr


class Robot:

    # a class attribute
    coordinate_z = 45.87

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f"walking coordinates ({self.x}, {self.y})")


# 1st instantiation
test_walk1 = Robot(8.9, 99.7)
print(test_walk1.coordinate_z)


# 2nd instantiation
test_walk2 = Robot(4.5, 6.7)
print(test_walk2.coordinate_z)
