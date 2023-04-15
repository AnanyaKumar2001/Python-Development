# -------------------------------------------------------------
# ---------**## Regular Expression Methods Part 1 ##**---------


import re


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 14 ->>>> findall()

# \d ->>>> [0-9]

# string = "hello 12 hi 65 123 howdy 784 907"
# string = "hello"
# pattern = "\d+"

# result = re.findall(pattern, string)

# print(result)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 15 ->>>> split()


# string = "hello 12 hi 65 123 howdy 784 907"
# string = "hello there"
# pattern = "\d+"

# result = re.split(pattern, string)
# print(result)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 16 ->>>> sub()

# sub(pattern, replace, string)

# string = "abc 12\
#   de 23 \n f45 621"

# print(string)

# pattern = "\s+"

# print(re.findall(pattern, string))

# replace = ""

# new_string = re.sub(pattern, replace, string)
# print(new_string)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 17 ->>>> sub()


# string = "abc 12\
#   de 23 \n f45 621"

# pattern = "\s+"
# replace = ""

# new_string = re.sub(pattern, replace, string, 1)
# new_string = re.sub(pattern, replace, string, 2)
# new_string = re.sub(pattern, replace, string, 3)
# new_string = re.sub(pattern, replace, string, 4)
# new_string = re.sub(pattern, replace, string, 5)
# print(new_string)
