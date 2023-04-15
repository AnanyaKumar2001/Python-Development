# ------------------------------------------------------------
# ----------------**## strptime() Method ##**-----------------


from datetime import datetime


# *-*-*-*-*-*-*-*-*-*-*- Example 21 ->>>> strptime()
# date_str = "21 December, 2111"
# print(type(date_str))

# date_obj = datetime.strptime(date_str, "%d %B, %Y")
# print(date_obj)
# print(type(date_obj))

# *-*-*-*-*-*-*-*-*-*-*- Example 22 ->>>> string to datetime object

# date_str = "11 Aug, 2099"

# date_obj = datetime.strptime(date_str, "%d %b, %Y")
# print(date_obj)


# *-*-*-*-*-*-*-*-*-*-*- Example 23 ->>>> string to datetime object

date_str1 = "18/01/2200 19:10:10"
date_str2 = "12/31/2200 10:19:19"

# considering the date is in dd/mm/yyyy format
date_obj1 = datetime.strptime(date_str1, "%d/%m/%Y %H:%M:%S")
print(date_obj1)
print(type(date_obj1))

# considering the date is in mm/dd/yyyy format
date_obj2 = datetime.strptime(date_str2, "%m/%d/%Y %H:%M:%S")
print(date_obj2)
print(type(date_obj2))
