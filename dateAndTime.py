from datetime import date
from datetime import time
from datetime import datetime

Today = date.today()
print("Today's date is ",Today)

print("Date:",Today.day,Today.month,Today.year)

print("Today's week day :",Today.weekday())

days = ["mon","tue","wed","thu","fri","sat","sun"]
print("which it is :",days[Today.weekday()])

Today = datetime.now()
print("The current date and time: ",Today)
