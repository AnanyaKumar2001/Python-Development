# ------------------------------------------------------------
# -----------**## Dictionary Methods Part 4 ##**--------------

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

# ******------****** Example 19 ->>>> pop()
# Case #1

# target_item1 = employee_info.pop("Age")
# print(target_item1)
# print(employee_info)


# ******------****** Example 20 ->>>> pop()
# Case #2

# target_item2 = employee_info.pop("Smoking", "No")
# print(target_item2)
# print(employee_info)


# ******------****** Example 21 ->>>> pop()
# Case #3

# target_item3 = employee_info.pop("Allergies")
# print(target_item3)
# print(employee_info)


# ******------****** Example 22 ->>>> pop()
# Case #4

# target_item4 = employee_info.pop("Best Friend", "COCO")
# print(target_item4)
# print(employee_info)


# ******------****** Example 23 ->>>> update()
# Case #1

# lost_key = {"Favorite Movie": "The Blood Diamond"}
# employee_info.update(lost_key)
# print(employee_info)


# ******------****** Example 24 ->>>> update()
# Case #2

# found_key = {"Favorite Movie": "Titanic"}
# employee_info.update(found_key)
# print(employee_info)

# ******------****** Example 25 ->>>> update()
# Case #3 ->>>> when a tuple is passed

employee_info.update(Dog_Name="Krypto", Bird_Name="Precious")
print(employee_info)
