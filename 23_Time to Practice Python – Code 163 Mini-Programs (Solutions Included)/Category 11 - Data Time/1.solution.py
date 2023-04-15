from time import gmtime, strftime
import datetime

print(datetime.datetime.now())


print(datetime.datetime.now().time())

# Method 2

print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
