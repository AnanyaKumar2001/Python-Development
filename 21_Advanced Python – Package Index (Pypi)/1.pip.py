# ------------------------------------------------------------
# -----------------------**## Pip ##**------------------------

import requests

from datetime import datetime
import pytz

response = requests.get("http://google.com")
print(response)

local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NYC = pytz.timezone("America/New_York")
datetime_NYC = datetime.now(tz_NYC)
print("NYC:", datetime_NYC.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
