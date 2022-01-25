import time
import calendar
#the datetime object enable us to customize date objects, perform various operations on dates
#like comparisons etc
from datetime import datetime as dt

#gives the number of ticks since 1 january 1970
print(time.time())
#THE LOCALTIME() FUNCTION gives the local of turple of 9 arguments
print(time.localtime(time.time()))
#THE ASC() FUNCTION enables us to format the time in our local time
print(time.asctime(time.localtime(time.time())))

#datetime objects usage examples
#creating date objects
#print(datetime.datetime.now())
#print(datetime.datetime(2030, 12, 10))
#print(datetime.datetime(2018, 12, 10))
#specifying the time along with the date
#print(dt.datetime(2030, 12, 10))
#print(dt.datetime(2019, 8,23,17,23,12))


#comparing two times
if dt(dt.now().year, dt.now().month, dt.now().day, 8)< dt.now()< dt(dt.now().year, dt.now().month, dt.now().day, 16):
    print('Working hours....')
else:
    print('Fun hours....')

#getting the calender of a particular month
#first, we import the calendar object from the calender module
cal = calendar.month(2019, 12)

#printing the calendar of the whole year
#we use the prcal() method by passing in the year whose calendar is be printed
calendar.prcal(2020)
print(cal)
for seconds in range(0, 5):
    print(seconds)
    #each element will be printed after 1 second
    #time.sleep(2)
    