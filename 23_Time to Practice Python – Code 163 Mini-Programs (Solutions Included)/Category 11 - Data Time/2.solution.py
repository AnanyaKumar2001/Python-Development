from datetime import datetime


date_string = "Feb 25 2300 4:20PM"
datetime_obj = datetime.strptime(date_string, "%b %d %Y %I:%M%p")

print(datetime_obj)
