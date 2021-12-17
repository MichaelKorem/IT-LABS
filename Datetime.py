from datetime import date, datetime

SchoolStart = "2000/9/7"
today = "2021/11/29"

start = datetime.strptime(SchoolStart, "%Y/%m/%d")
end = datetime.strptime(today, "%Y/%m/%d")

total = end.date() - start.date()
print("You have been in school for:", total.days, "days!")

#-----------------------------------------------------------

def diff_dates(date1, date2):
    return abs (date2-date1).days

day1 = int(input("Please enter the starting day: "))
month1 = int(input("Please enter the starting month: "))
year1 = int(input("Please enter the starting year: "))

day2 = int(input("Please enter the ending day: "))
month2 = int(input("Please enter the ending month: "))
year2 = int(input("Please enter the ending year: "))

d1 = date(year1,month1,day1)
d2 = date(year2,month2,day2)

result = diff_dates(d2,d1)
print("There are {} days between {} and {}".format(result, d1, d2))

#-------------------------------------------------------------------

day = int(input("Please enter the day: "))
month = int(input("Please enter the month: "))
year = int(input("Please enter the year: "))
hour = int(input("Please enter the hour: "))
minute = int(input("Please enter the minute: "))
second = int(input("Please enter the second: "))
microsecond = int(input("Please enter the ms: "))

dt = datetime(year,month,day,hour,minute,second,microsecond)
print("The date in a nice format is: ", dt.strftime("%A %B %d %Y, %H:%M:%S"))
