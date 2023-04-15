# ------------------------------------------------------------
# -------------------**## Time Class ##**---------------------

from datetime import time

# *-*-*-*-*-*-*-*-*-*-*- Example 8 ->>>> Time object to represent time
time_1 = time()
print("Time A:", time_1)


time_2 = time(13, 55, 00)
print("Time B:", time_2)


time_3 = time(hour=9, minute=51, second=15)
print("Time C:", time_3)


time_4 = time(13, 55, 00, 100000)
print("Time D:", time_4)


# *-*-*-*-*-*-*-*-*-*-*- Example 9 ->>>> getting hour, minute, second and microsecond

time_5 = time(11, 34, 56)

print("Hour:", time_5.hour)
print("Minute:", time_5.minute)
print("Second:", time_5.second)
print("Microsecond:", time_5.microsecond)
