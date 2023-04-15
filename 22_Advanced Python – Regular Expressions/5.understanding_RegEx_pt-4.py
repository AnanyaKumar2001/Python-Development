# -------------------------------------------------------------
# ------**## Understanding Regular Expressions Part 4 ##**-----

import re


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 11 ->>>> | - Alternation

# match_result = re.finditer("a|b", "adc")
# match_result = re.finditer("z|c", "adc")
# match_result = re.finditer("z|c", "zzc")
# match_result = re.finditer("z|c|t", "zcctv")


# for match in match_result:
#     print(match)

# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 12 ->>>> () - Group


# match_result = re.finditer("(a|b|c)xz", "abc xz")
# match_result = re.finditer("(a|b|c)xz", "abcxz")
# match_result = re.finditer("(a|b|c)xz", "abxz")
# match_result = re.finditer("(a|b|c)xz", "axz")
# match_result = re.finditer("(a|b|c)xz", "axz cabxz")


# for match in match_result:
#     print(match)


# ------------------------------------------------------------
# *-*-*-*-*-*-* Example 13 ->>>> \ - Backslash

match_result = re.match("\^xz", "^xz")

print(match_result)
