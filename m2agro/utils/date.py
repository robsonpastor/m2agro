# -*- coding: utf-8 -*- 
import datetime
import calendar

def add_months(sourcedate,months):
    month = sourcedate.month - 1 + months
    year = int(sourcedate.year + month / 12 )
    month = month % 12 + 1
    day = min(sourcedate.day,calendar.monthrange(year,month)[1])
    return datetime.date(year,month,day)

def lenient_date(year, month, day):
    if month>12:
        year = year + month/12
        month = month % 12
        
    try:
        return datetime.date(year, month, day)
    except:
        return datetime.date(year, month+1, 1) - datetime.timedelta(days=1)
