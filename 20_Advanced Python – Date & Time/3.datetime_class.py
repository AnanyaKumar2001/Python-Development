# ------------------------------------------------------------
# -----------------**## Datetime Class ##**-------------------

from datetime import datetime


# *-*-*-*-*-*-*-*-*-*-*- Example 10 ->>>> Python datetime object
time_1 = datetime(2100, 1, 1)
print(time_1)


time_2 = datetime(2050, 10, 25, 20, 50, 50)
print(time_2)

# *-*-*-*-*-*-*-*-*-*-*- Example 11 ->>>> getting year, month, hour, minute and timestamp

time_3 = datetime(2050, 10, 25, 23, 13, 50)

print("year:", time_3.year)
print("month:", time_3.month)
print("day:", time_3.day)
print("hour:", time_3.hour)
print("minute:", time_3.minute)
print("second:", time_3.second)
print("timestamp:", time_3.timestamp())
