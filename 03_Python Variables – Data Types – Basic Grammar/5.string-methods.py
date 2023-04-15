# ------------------------------------------------------------
# -----------------**## String Methods ##**-------------------

# 1- len()
address = "Afghanistan"
# print(len(address))

# 2- [] Notation
# print(address[0])
# print(address[7])
# print(address[-1])
# print(address[-4])

# 3- [] Notation
# print(address[0:4])
# print(address[-7:-1])
# print(address[0:])
# print(address[:9])
# print(address[:])

# 4- Concatenation ->>>> Formatted Strings
country = "USA"
city = "NYC"
# full_address = city + ", " + country
full_address = f"{city}, {country}"
print(full_address)

# 5- upper()
# print(address.upper())

# 6- lower()
# print(city.lower())

# 7- title()
# print(full_address.title())

# 8- strip()
job = "       Programmer   "
# print(job)
# print(job.strip())
# print(job.lstrip())
# print(job.rstrip())

# 9- find()
# print(address.find("n"))
# print(address.find("i"))

# 10- replace()
# print(address.replace("f", "Z"))

# 11- in operator
# print("ne" in address)
# print("ni" in address)

# 12- not operator
# print("ne" not in address)
# print("ni" not in address)
