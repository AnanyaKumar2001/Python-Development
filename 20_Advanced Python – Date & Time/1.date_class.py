# ------------------------------------------------------------
# -------------------**## Date Class ##**---------------------


# *-*-*-*-*-*-*-*-*-*-*- Example 1 ->>>> Getting the current Date & Time
# from datetime import datetime

# print(datetime.now())

# *-*-*-*-*-*-*-*-*-*-*- Example 2 ->>>> Getting the current Date
# import datetime

# print(datetime.date.today())

# *-*-*-*-*-*-*-*-*-*-*- Example 3 ->>>> Getting the Datetime attributes
# import datetime

# print(dir(datetime))

# *-*-*-*-*-*-*-*-*-*-*- Example 4 ->>>> Creating a date object
# import datetime


# date = datetime.date(2100, 12, 31)

# print(date)
# print(type(date))


# *-*-*-*-*-*-*-*-*-*-*- Example 5 ->>>> importing the date class
# from datetime import date

# print(date(2100, 12, 30))

# *-*-*-*-*-*-*-*-*-*-*- Example 6 ->>>> getting date from a timestamp
# from datetime import date

# time_stamp = date.fromtimestamp(5198811999)
# print(time_stamp)

# *-*-*-*-*-*-*-*-*-*-*- Example 7 ->>>> getting today's year, month and day

from datetime import date
today = date.today()

print("Current Year:", today.year)
print("Current Month:", today.month)
print("Current Day:", today.day)
