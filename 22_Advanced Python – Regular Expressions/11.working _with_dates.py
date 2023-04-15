# -------------------------------------------------------------
# ---------------**## Working with Dates ##**------------------

import re


# dates = """
# 15/10/2100

# 06/29/2099

# 01-01-1975

# 08-31-1299

# 15.10.2035

# 09_12_1885

# 2020/01/16

# 2020-17-11
# """

with open("dates.txt") as file:
    # print(file)
    # print(file.read())
    # print(type(file.read()))
    dates = file.read()

    matches_result = re.finditer(r"\d\d.\d\d.\d\d\d\d", dates)
    matches_result = re.finditer(r"\d{2}.\d{2}.\d{4}", dates)
    matches_result = re.finditer(r"\d{2}/\d{2}/\d{4}", dates)
    matches_result = re.finditer(r"\d{2}-\d{2}-\d{4}", dates)
    matches_result = re.finditer(r"\d{2}\.\d{2}\.\d{4}", dates)
    matches_result = re.finditer(r"\d{2}[/-]\d{2}[/-]\d{4}", dates)
    matches_result = re.finditer(r"\d{4}[/-]\d{2}[/-]\d{2}", dates)

    for match in matches_result:
        print(match)
