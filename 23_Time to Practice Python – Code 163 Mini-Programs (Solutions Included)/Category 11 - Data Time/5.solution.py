from datetime import datetime

given_date = datetime(2100, 12, 15)

print(given_date.today().weekday())

print(given_date.strftime("%A"))
