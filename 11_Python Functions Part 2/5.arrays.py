# ------------------------------------------------------------
# -----------------------**## Arrays ##**---------------------


# ******------****** Example 12
from array import array

# https://docs.python.org/3/library/array.html

numbers = array("i", [1, 2, 3])
numbers.append(4)
print(numbers)

# numbers[0] = 2.3 # TypeError
