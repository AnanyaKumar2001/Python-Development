from datetime import datetime, timedelta

given_date = datetime(2050, 3, 15, 10, 0, 0)

days_to_add = 7
resulting_date = given_date + timedelta(days=days_to_add, hours=12)
print(resulting_date)
