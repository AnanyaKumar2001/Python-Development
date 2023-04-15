# ------------------------------------------------------------
# -----------------**## Timedelta Class ##**------------------

from datetime import timedelta, date, datetime


# *-*-*-*-*-*-*-*-*-*-*- Example 12 ->>>> Difference between two dates and times
# t1 = date(year=2060, month=12, day=15)
# t2 = date(year=1970, month=1, day=1)

# t3 = t1 - t2
# print(t3)
# print(type(t3))


# t1 = datetime(year=2060, month=12, day=15, hour=5, minute=39, second=31)
# t2 = datetime(year=1970, month=1, day=1, hour=10, minute=10, second=10)

# t3 = t1 - t2
# print(t3)
# print(type(t3))


# *-*-*-*-*-*-*-*-*-*-*- Example 13 ->>>> Difference between two timedelta objects
# t1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
# t2 = timedelta(days=5, hours=11, minutes=12, seconds=33)

# t3 = t1 - t2
# print(t3)
# print(type(t3))

# *-*-*-*-*-*-*-*-*-*-*- Example 14 ->>>> getting negative timedelta object
t1 = timedelta(seconds=33)
t2 = timedelta(seconds=54)

t3 = t1 - t2
print(t3)

# *-*-*-*-*-*-*-*-*-*-*- Example 15 ->>>> Time duration in seconds

time = timedelta(days=110, hours=25, minutes=110, seconds=10000)

print("total seconds:", time.total_seconds())
