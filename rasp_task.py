import calendar
import datetime


def weekday():
    now = datetime.datetime.now()
    check = calendar.weekday(now.year, now.month, now.day)
    if check is 0:
        return "Monday"
    elif check is 1:
        return "Tuesday"
    elif check is 2:
        return "Wednesday"
    elif check is 3:
        return "Thursday"
    elif check is 4:
        return "Friday"
    elif check is 5:
        return "Saturday"
    elif check is 6:
        return "Sunday"
    else:
        return "???"
