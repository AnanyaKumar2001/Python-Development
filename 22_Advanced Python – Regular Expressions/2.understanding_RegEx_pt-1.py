# -------------------------------------------------------------
# ------**## Understanding Regular Expressions Part 1 ##**-----

import re


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 2 ->>>> [] - Square brackets

# match_result = re.finditer("[abc]", "a")
# match_result = re.finditer("[abc]", "ac")
# match_result = re.finditer("[abc]", "hey there")
# match_result = re.finditer("[abc]", "abc de ca")
# match_result = re.finditer("[a-e]", "abc de ca cat dog elephant")
# match_result = re.finditer("[0-2]", "88 99 11 22 34 15 10")
# match_result = re.finditer("[^abc]", "abc de ca cat dog elephant")
# match_result = re.finditer("[^a-e]", "abc de ca cat dog elephant")
# match_result = re.finditer("[^0-5]", "88 99 116 227 34 15 10")


# for match in match_result:
#   print(match)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 3 ->>>> . - Period

match_result = re.finditer(".", "123")
match_result = re.finditer(".", "abc")
match_result = re.finditer("..", "abc")
match_result = re.finditer("..", "abcd")

for match in match_result:
    print(match)
