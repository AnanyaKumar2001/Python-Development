from datetime import datetime

from dateutil.relativedelta import relativedelta

given_date = datetime(2035, 5, 20).date()

months_to_add = 4

new_date = given_date + relativedelta(months=months_to_add)

print(new_date)
