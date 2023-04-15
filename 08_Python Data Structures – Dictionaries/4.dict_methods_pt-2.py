# ------------------------------------------------------------
# -----------**## Dictionary Methods Part 2 ##**--------------

employee_info = {
    "Name": "Will",
    "Last Name": "Oldman",
    "Address": "New York, USA",
    "Job": {"Salesperson", "Developer"},
    "Age": 34,
    "Hobbies": ("Reading", "Wacthing Movies", "Walking"),
    1992: "Date of Birth",
    "Married": True,
    "Favorite Songs": ["Un Dia", "Blinding Lights", "Shallow"],
    "Best Friend": {"Name": "Gerald"},
    "Special One": None
}

# ******------****** Example 11 ->>>> items()

# print(employee_info.items())

# ******------****** Example 12 ->>>> items()

# del employee_info['Best Friend']

# print(employee_info.items())


# ******------****** Example 13 ->>>> keys()

# print(employee_info.keys())

# ******------****** Example 14 ->>>> keys()

del employee_info["Hobbies"]

print(employee_info.keys())
