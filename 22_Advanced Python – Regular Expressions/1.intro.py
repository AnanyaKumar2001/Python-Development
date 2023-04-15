# -------------------------------------------------------------
# ----**## Introduction to Regular Expressions (RegEx) ##**----

import re

# *-*-*-*-*-*-* Example 1

test_string = "tan"
test_string = "cat"
test_string = "dog"
test_string = "dag"

pattern = ".a."
result = re.match(pattern, test_string)
print(result)
