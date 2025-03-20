import datetime

def find_day(date_str):
    month, day, year = map(int, date_str.split())
    date = datetime.date(year, month, day)
    return date.strftime("%A")