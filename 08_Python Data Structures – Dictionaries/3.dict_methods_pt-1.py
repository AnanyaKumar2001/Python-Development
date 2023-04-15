# ------------------------------------------------------------
# -----------**## Dictionary Methods Part 1 ##**--------------

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

# ******------****** Example 8 ->>>> clear()

# employee_info.clear()
# print(employee_info)


# ******------****** Example 9 ->>>> copy()

gerald_info = employee_info.copy()
gerald_info["Best Friend"] = "Will Oldman"
# print(gerald_info)
# print(employee_info)

# ******------****** Example 10 ->>>> fromkeys()

letters = {'a', 'e', 'i', 'o', 'u'}
numbers = [1, 2]

vowels = dict.fromkeys(letters)
vowels = dict.fromkeys(letters, numbers)
print(vowels)

print({}.fromkeys(employee_info))
