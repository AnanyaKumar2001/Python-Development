from datetime import datetime, timedelta

given_date = datetime(2100, 2, 25)
daya_to_subtract = 7

resulting_date = given_date - timedelta(days=daya_to_subtract)

print(resulting_date)
