# -------------------------------------------------------------
# ---------------**## Working with Emails ##**-----------------

import re

with open("emails.txt") as file:
    emails = file.read()

    pattern = r"[a-zA-Z0-9]+@"
    pattern = r"[a-zA-Z0-9-_]+@"
    pattern = r"[a-zA-Z0-9-_\.]+@"
    pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-]+"
    pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-]+\."
    pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-]+\.com"
    pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-]+\.(com|edu|io)"
    pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-]+\.[a-z]+"
    pattern = r"([a-zA-Z0-9-_\.]+)@([a-zA-Z-]+)\.([a-z]+)"

    matches_result = re.finditer(pattern, emails)

    for match in matches_result:
        # print(match)
        # print(match.group())
        # print(match.group(0))
        # print(match.group(1))
        # print(match.group(2))
        print(match.group(3))
