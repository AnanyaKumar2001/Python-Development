# ------------------------------------------------------------
# ----------------**## strftime() Method ##**-----------------

# Date Formats
# US ->>>> mm/dd/yyyy
# UK ->>>> dd/mm/yyyy

from datetime import datetime

# *-*-*-*-*-*-*-*-*-*-*- Example 16 ->>>> formatting date using strftime()
# current date & time
# now = datetime.now()

# time = now.strftime("%H:%M:%S")
# print(time)

# s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# print(s1)
# print(type(s1))

# *-*-*-*-*-*-*-*-*-*-*- Example 17 ->>>> datetime to string using strftime()
now = datetime.now()

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")


# *-*-*-*-*-*-*-*-*-*-*- Example 18 ->>>> creating string from a timestamp
# timestamp = 4313259999
# date_time = datetime.fromtimestamp(timestamp)

# print(date_time)
# print(type(date_time))

# date = date_time.strftime("%m/%d/%Y, %H:%M:%M")
# print(date)
# print(type(date))

# read more about date and time on the python docs and find more directives
# https://docs.python.org/3/library/datetime.html

# date2 = date_time.strftime("%d %b, %Y")
# print(date2)

# date3 = date_time.strftime("%d %B, %Y")
# print(date3)

# time2 = date_time.strftime("%I%p")
# print(time2)


# *-*-*-*-*-*-*-*-*-*-*- Example 19 ->>>> locale's appropriate date and time
# timestamp = 4599998989
# date_time = datetime.fromtimestamp(timestamp)

# d1 = date_time.strftime("%c")
# print(d1)

# # dd/mm/year
# d2 = date_time.strftime("%x")
# print(d2)

# # hh:mm:ss
# d3 = date_time.strftime("%X")
# print(d3)

# *-*-*-*-*-*-*-*-*-*-*- Example 20 ->>>> python datetime to timestamp

now = datetime.now()

# converting to timestamp
time_stamp = datetime.timestamp(now)
print(time_stamp)


# converting from timestamp
date_time = datetime.fromtimestamp(time_stamp)
print(date_time)
