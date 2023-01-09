from datetime import datetime
#import calendar


def get_days_in_month(month, year):
    date_start = datetime(year=int(year), month=int(month), day=1)
    if month == 12:
        date_end = datetime(year=int(year+1), month=1, day=1)
    else:
        date_end = datetime(year=int(year), month=int(month+1), day=1)
    diff = date_end - date_start
    res_days = diff.days
    return res_days


print(get_days_in_month(12, 2022))
