# ------------------------------------------------------------
# ------------------**## Data Classes ##**--------------------


# --**--**--**--**--** Example 41 ->>>> issue
# class Robot:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

# robot1 = Robot(1, 2)
# robot2 = Robot(1, 2)

# print(robot1 == robot2)

# print(id(robot1))
# print(id(robot2))

# --**--**--**--**--** Example 42 ->>>> Solution 1 -> __eq__


# class Robot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# robot1 = Robot(1, 2)
# robot2 = Robot(1, 2)

# print(robot1 == robot2)


# --**--**--**--**--** Example 43 ->>>> Solution 2 -> namedtuple()

from collections import namedtuple

Robot = namedtuple("Robot", ["x", "y"])

robot1 = Robot(x=1, y=2)
robot2 = Robot(1, 2)

print(robot1 == robot2)
