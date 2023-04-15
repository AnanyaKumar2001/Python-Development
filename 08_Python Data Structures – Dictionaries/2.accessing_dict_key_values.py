# ------------------------------------------------------------
# ---------**## Accessing Dictionary Key-Values ##**----------


employee_info = {
    "Name": "Will",
    "Last Name": "Oldman",
    "Address": "New York, USA",
    "Job": "Salesperson",
    "Age": 34
}


# ******------****** Example 4

# print(employee_info["Name"])
# print(employee_info["Job"])

# ******------****** Example 5

employee_info["Job"] = "Developer"
employee_info["Hobbies"] = "Reading", "Walking"
# print(employee_info)


# ******------****** Example 6
# print(employee_info["Favorite Color"])

# 1- checking whether a key exists

# if "Favorite Color" in employee_info:
#     print("Favorite Color")

# 2- get()
# print(employee_info.get("Favorite Color"))

# ******------****** Example 7
print(employee_info.get("Favorite Color", "Green"))
