# imports
from datetime import date, datetime, timedelta, timezone
import time
import calendar as cal
from zoneinfo import ZoneInfo

# date
today = date.today()
print(today)

date_a = date(2021, 3, 28)
print(date_a.ctime())

print(today.isoformat())
print(today.weekday())

print(cal.day_name[today.weekday()])
print(today.day, today.month, today.year)
print(today.timetuple())

# time
print(time.ctime())
print(time.daylight)

print(time.gmtime())
print(time.gmtime(0))

print(time.localtime())
print(time.time())

# datetime, timezones and tiemdeltas
now = datetime.now()
print(now)

utcnow = datetime.utcnow()
print(utcnow)

print(now.date())
print(now.day, now.month, now.year)

print(now.date() == date.today())

print(now.time())
print(now.hour, now.minute, now.second, now.microsecond)

print(now.ctime())
print(now.isoformat())

print(now.timetuple())
print(now.tzinfo)
print(utcnow.tzinfo)

print(now.weekday())
f_bday = datetime(1975, 12, 29, 12, 50, tzinfo=ZoneInfo('Europe/Rome'))
h_bday = datetime(1981, 10, 7, 15, 30, 50, tzinfo=timezone(timedelta(hours=2)))
diff = h_bday - f_bday
print(diff)
print(type(diff))

print(diff.days)
print(diff.total_seconds())

print(today + timedelta(days=49))
print(now + timedelta(weeks=7))

# parsing (stdlib)
print(datetime.fromisoformat('1977-11-24T19:30:13+01:00'))
print(datetime.fromtimestamp(time.time()))

print(datetime.now())

# arrow small demo
import arrow

print(arrow.utcnow())
print(arrow.now())

local = arrow.now('Europe/Rome')
print(local)

print(local.to('utc'))
print(local.to('Europe/Moscow'))
print(local.to('Asia/Tokyo'))

print(local.datetime)
print(local.isoformat())