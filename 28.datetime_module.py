from calendar import month
import datetime

# curdatetime = datetime.datetime.now()
# print(curdatetime)

# createdTime = datetime.datetime(2022,6,30)
# print(createdTime)

# Python Dates
# This method is called strftime() and it takes a parameter, format, to specify the format of the returned string.
    # %b Month name, short version Dec
    # %B Month name, full version December
    # %m Month as a number 01 - 12
    # %y Year short version without century 22
    # %Y Year Full year 2022
    # %H Hour 0 - 23
    # %I Hour 00 - 12
    # %p AM/PM PM
    # %M 00 - 49     41

now = datetime.datetime.now()
print(now)
year = now.strftime("%Y")
m = now.strftime("%m")
d = now.day
print(year,"/",m,"/",d)