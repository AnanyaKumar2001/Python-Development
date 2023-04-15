set_one = {10, 20, 30, 40, 50}
set_two = {60, 70, 80, 90, 10}

if set_one.isdisjoint(set_two):
    print("The 2 sets have no common elements")
else:
    print("Common elements are", set_one.intersection(set_two))
