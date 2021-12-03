from datetime import date, datetime

now = datetime.datetime.now()

print(now.strftime("%m:%d:%Y, %H:%M:%S"))