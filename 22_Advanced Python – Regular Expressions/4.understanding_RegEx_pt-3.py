# -------------------------------------------------------------
# ------**## Understanding Regular Expressions Part 3 ##**-----

import re


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 7 ->>>> + - Plus

# match_result = re.finditer("ma+n", "mn")
# match_result = re.finditer("ma+n", "man")
# match_result = re.finditer("ma+n", "maaaan")
# match_result = re.finditer("ma+n", "main")
# match_result = re.finditer("ma+n", "woman")


# for match in match_result:
#     print(match)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 8 ->>>> ? - Question Mark

# match_result = re.finditer("ma?n", "mn")
# match_result = re.finditer("ma?n", "man")
# match_result = re.finditer("ma?n", "maaaan")
# match_result = re.finditer("ma?n", "main")
# match_result = re.finditer("ma?n", "woman")


# for match in match_result:
#     print(match)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 9 ->>>> {} - Braces


# match_result = re.finditer("a{2,4}", "abc dat")
# match_result = re.finditer("a{2,4}", "abc daat")
# match_result = re.finditer("a{2,4}", "aabc daaat")
# match_result = re.finditer("a{2,4}", "aabc daaat caaaat")
# match_result = re.finditer("a{2,4}", "aabc daaat caaaat daaaaag")


# for match in match_result:
#     print(match)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 10 ->>>> {} - Braces

match_result = re.finditer("[0-9]{2,4}", "abc 123 def ghi 45")
match_result = re.finditer("[0-9]{2,4}", "12 345 60789 12398 455 1")


for match in match_result:
    print(match)
