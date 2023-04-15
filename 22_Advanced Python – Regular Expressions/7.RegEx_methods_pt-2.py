# -------------------------------------------------------------
# ---------**## Regular Expression Methods Part 2 ##**---------


import re


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 18 ->>>> subn()


# string = "abc 12 de 23 f45 "
# pattern = '\s+'
# replace = ''

# new_string = re.subn(pattern, replace, string)
# print(new_string)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 19 ->>>> search()


# string = "is fun python"
# pattern = "\Apython"
# pattern = "python"
# match_result1 = re.search(pattern, string)
# match_result2 = re.match(pattern, string)

# print(match_result1)
# print(match_result2)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 20 ->>>> match.group()

# string = "12345 67, 7894 1122"
# pattern = "(\d{3}) (\d{2})"

# match = re.search(pattern, string)
# print(match)

# if match:
#     print(match.group())

#     print(match.start())
#     print(match.end())
#     print(match.span())
# else:
#     print("Match not found")
