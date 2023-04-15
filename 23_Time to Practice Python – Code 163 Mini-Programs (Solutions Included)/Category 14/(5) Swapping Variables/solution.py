x = input("Enter Anything: ")
y = input("Enter Anything: ")

print(f"Before Swapping, First Anything = '{x}' & Second Anything = '{y}'")

# Approach one ->>>> using a temp variable

# temp = x
# x = y
# y = temp

# print(f"After Swapping, First Anything = '{x}' & Second Anything = '{y}'")

# Approach Two ->>>> not using a temp variable

x, y = y, x

print(f"After Swapping, First Anything = '{x}' & Second Anything = '{y}'")
