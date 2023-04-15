# ------------------------------------------------------------
# ---------------------**## Classes ##**----------------------

"""
Object
1- attributes
2- behaviour
"""

"""
---------------------------------------------
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* Class
---------------------------------------------

A class is a blueprint for creating objects
"""


class Robot:
    pass


"""
---------------------------------------------
*-*-*-*-*-*-*-*-*-*-*-*-*-*-* Object/Instance
---------------------------------------------

An object (instance) is an instantiation of a class.
"""

robot_obj = Robot()

# print(robot_obj)
# print(type(robot_obj))


# --**--**--**--**--** # --**--**--**--**--**

# class of str for creating strings
name = "Muslim"
print(type(name))


# class of int for creating intergers
x = 25
print(type(x))


# class of float for creating floating point numebrs
y = 3.5
print(type(y))

# class of bool for creating booleans
z = True
print(type(z))


# class of list for creating lists
my_list = [1, 2, 3]
print(type(my_list))

# class of dict for creating dicts
my_info = {
    "name": "Muslim",
    "last name": "Helalee"
}
print(type(my_info))

# class of tuple for creating tuples
my_tuple = (1, 2, 3)
print(type(my_tuple))

# class of set for creating sets
my_set = {1, 2, 3}
print(type(my_set))


"""
---------------------------------------------
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* Summary
---------------------------------------------

Class ->>> is a blueprint for creating new objects

Object ->>> is an instance of a class


Class === Robot

Object === attributes and behaviors of the Robot

"""
