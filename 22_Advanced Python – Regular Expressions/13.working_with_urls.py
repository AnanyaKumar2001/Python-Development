# -------------------------------------------------------------
# ----------------**## Working with URLs ##**------------------

import re

with open("urls.txt") as file:
    urls = file.read()

    pattern = r"http://([a-zA-Z]+)\."
    pattern = r"https?://([a-zA-Z]+)\."
    pattern = r"https?://([a-zA-Z]+)\.([a-zA-Z0-9-]+)"
    pattern = r"https?://(www\.)?([a-zA-Z]+)\.([a-z]+)"

    matches_result = re.finditer(pattern, urls)

    for match in matches_result:
        # print(match)
        # print(match.group())
        # print(match.group(1))
        print(match.group(2))
