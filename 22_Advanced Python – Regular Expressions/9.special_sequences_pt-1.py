# -------------------------------------------------------------
# -------------**## Special Sequences Part 1 ##**--------------

import re


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 22 ->>>> \d - [0-9]

# match_result = re.finditer(r"\d", "12 3.4 5 67.8 90")

# for match in match_result:
#     print(match)

# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 23 ->>>> \D - [a-zA-Z_ ] + symbols


# match_result = re.finditer(r"\D", "12 45 # HI There < ? _")

# for match in match_result:
#     print(match)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 24 ->>>> \s - (space, tab, " ", "\t", "\n")

# match_result = re.finditer(r"\s", "12 45 # HI There \t \n < ? _")

# for match in match_result:
#     print(match)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 25 ->>>> \S - [a-zA-Z0-9_] + symbols


match_result = re.finditer(r"\S", "12 45 # HI There \t \n < ? _")

for match in match_result:
    print(match)
