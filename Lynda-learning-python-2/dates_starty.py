#
#
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    print(today)
    print('Date components:', today.day, today.month, today.year)
    print('Today is day: ', today.weekday())
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    print('Today is day: ', days[today.weekday()])

    today = datetime.now()
    print(today)
    t = datetime.time(datetime.now())
    print(t)




main()
