# import cmath
import math


a = int(input("a: "))

if a <= 0:
    print("The value of the constant 'a' cannot be zero or less")
else:
    b = int(input("b: "))
    c = int(input("c: "))

    discriminant = (b**2) - (4*a*c)

    solution_one = (-b-math.sqrt(discriminant)) / (2*a)
    solution_two = (-b+math.sqrt(discriminant)) / (2*a)

    print(f"The solutions are {solution_one} & {solution_two}")
