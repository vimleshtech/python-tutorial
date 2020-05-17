import datetime

datetime_object = datetime.datetime.now()
print(datetime_object) #yyy-mm-dd hh:mm

date_object = datetime.date.today()
print(date_object)

print(dir(datetime))

#convert to date
d = datetime.date(2019, 4, 13)
print(d)


timestamp = datetime.date.fromtimestamp(1326244364)
print("Date =", timestamp)

#pring year month day
# date object of today's date
today = datetime.date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


#print hour min sec
a = datetime.time(11, 34, 56)

print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)


#diff of dates
from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)


#diff of dates
from datetime import date

d0 = date(2008, 8, 18)
d1 = date(2008, 9, 26)
delta = d1 - d0
print (delta.days)


#diff of dates
from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)

#format

from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)





