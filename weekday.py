# this program checks the what day it is
# it then prints a message depending on whether it is a weekday or a weekend day

# author: Philip Cullen

import datetime

week_days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
now = datetime.datetime.now()
day = week_days[now.weekday()]
if day in ("Saturday", "Sunday"):
    print("Yay, it is the weekend!")
else :
    print("Unfortunately, it is a weekday.")
