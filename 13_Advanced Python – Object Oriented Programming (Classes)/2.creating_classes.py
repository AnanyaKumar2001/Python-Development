# ------------------------------------------------------------
# -----------------**## Creating Classes ##**-----------------


# --**--**--**--**--** Example 1

class Robot:
    def walk(self):
        print("The robot is walking")


robot = Robot()

robot.walk()

print(type(robot))

# --**--**--**--**--** Example 2 ->>>> isinstance()

print(isinstance(robot, Robot))

robot_obj = Robot()

print(isinstance(robot_obj, Robot))
