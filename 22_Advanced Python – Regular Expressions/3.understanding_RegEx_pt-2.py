# -------------------------------------------------------------
# ------**## Understanding Regular Expressions Part 2 ##**-----

import re


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 4 ->>>> ^ - Caret


# match_result = re.finditer("^a", "a")
# match_result = re.finditer("^a", "abc")
# match_result = re.finditer("^a", "bac")
# match_result = re.finditer("^ab", "abc")
# match_result = re.finditer("^ab", "acb")

# for match in match_result:
#     print(match)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 5 ->>>> $ - Dollar


# match_result = re.finditer("a$", "a")
# match_result = re.finditer("a$", "formula")
# match_result = re.finditer("a$", "cab")

# for match in match_result:
#     print(match)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 6 ->>>> * - Star

match_result = re.finditer("ma*n", "mn")
match_result = re.finditer("ma*n", "man")
match_result = re.finditer("ma*n", "maaaaan")
match_result = re.finditer("ma*n", "main")
match_result = re.finditer("ma*n", "woman")


for match in match_result:
    print(match)
