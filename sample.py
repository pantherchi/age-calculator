import datetime
from datetime import date

cD = date(2015, 3, 15)
bD = date(2016, 3, 15)
dayCalc = bD - cD
print(dayCalc.days)
