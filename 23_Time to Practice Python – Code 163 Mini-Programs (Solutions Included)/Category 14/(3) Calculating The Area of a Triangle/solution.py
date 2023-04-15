side_one = int(input("Side One: "))
side_two = int(input("Side Two: "))
side_three = int(input("Side Three: "))

semi_perimeter = (side_one + side_two + side_three) / 2

triangle_area = round((semi_perimeter * (semi_perimeter - side_one) *
                       (semi_perimeter - side_two) * (semi_perimeter - side_three)) ** 0.5)

print(f"The area of the triangle is {triangle_area}")
