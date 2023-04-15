from datetime import datetime

given_date = datetime(2035, 5, 20)

string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")

print(string_date)
print(type(string_date))
