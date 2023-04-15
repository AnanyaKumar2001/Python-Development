# ------------------------------------------------------------
# --------**## Instance Methods VS Class Methods ##**---------


# --**--**--**--**--** Example 9 ->>>> instance methods


# class Robot:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y


#   def walk(self):
#     print(f"walking coordinates ({self.x}, {self.y})")


# test_walk = Robot(1.1, 4.6)
# test_walk.walk()


# --**--**--**--**--** Example 10 ->>>> class methods


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # decorator
    @classmethod
    def specific_coordiante(cls):
        return cls(1.1, 4.6)

    def walk(self):
        print(f"walking coordinates ({self.x}, {self.y})")


test_walk = Robot.specific_coordiante()
test_walk.walk()
