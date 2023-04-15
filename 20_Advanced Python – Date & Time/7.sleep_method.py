# ------------------------------------------------------------
# -------------------**## sleep() Method ##**-----------------

import time


# *-*-*-*-*-*-*-*-*-*-*- Example 24 ->>>> sleep()
# print("printed immediately")
# time.sleep(2.0)
# print("printed after 2 seconds")

# *-*-*-*-*-*-*-*-*-*-*- Example 25 ->>>> creating a simple low level digital clock
while True:
    local_time = time.localtime()
    result = time.strftime("%I:%M:%S", local_time)
    print(result)
    time.sleep(1)
