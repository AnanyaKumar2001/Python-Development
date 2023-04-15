# -------------------------------------------------------------
# -------------**## Special Sequences Part 2 ##**--------------

import re


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 26 ->>>> \w - [a-zA-Z0-9_]

# match_result = re.finditer(r"\w", "12 54 # \n Theme < ? _")

# for match in match_result:
#     print(match)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 27 ->>>> \W - not [a-zA-Z0-9_]

# match_result = re.finditer(r"\W", "12 54 # \n Theme < ? _")

# for match in match_result:
#     print(match)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 28 ->>>> \b

# *-*-*-*- Case 1 - At the beginning

# string = "possible 12 54 # .  hi possible \n There possible \t < ? _ > % ^  impossible"

# match_result = re.finditer(r"\bpossible", string)


# *-*-*-*- Case 2 - At the end

# string = "possibleis 12 54 # .  hi  \n There possible \t < ? _ > % ^  impossible"

# match_result = re.finditer(r"possible\b", string)


# for match in match_result:
#     print(match)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 29 ->>>> \B

# *-*-*-*- Case 1 - Not at the beginning

string = "heater 12 54 # .  hi \n There \t < ? _ > % ^  unheated noheat"

# match_result = re.finditer(r"\Bheat", string)


# *-*-*-*- Case 2 - Not at the end

match_result = re.finditer(r"heat\B", string)

for match in match_result:
    print(match)
