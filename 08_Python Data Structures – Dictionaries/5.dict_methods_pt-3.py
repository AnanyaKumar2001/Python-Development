# ------------------------------------------------------------
# -----------**## Dictionary Methods Part 3 ##**--------------

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

# ******------****** Example 15 ->>>> values()

# print(employee_info.values())


# ******------****** Example 16 ->>>> values()

# del employee_info["Age"]

# print(employee_info.values())


# ******------****** Example 17 ->>>> popitem()

# print(employee_info.popitem())
# print(employee_info)


# ******------****** Example 18 ->>>> setdefault()

# print(employee_info.setdefault("Age"))


# print(employee_info.setdefault("Smoking"))

# print(employee_info.setdefault("Allergies", "N/A"))

# print(employee_info.setdefault("Name", "Ryan"))

# print(employee_info)
