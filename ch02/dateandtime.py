
# imports
>>> from datetime import date, datetime, timedelta, timezone
>>> import time
>>> import calendar as cal
>>> from zoneinfo import ZoneInfo


# date
>>> today = date.today()
>>> today
datetime.date(2021, 3, 28)
>>> today.ctime()
'Sun Mar 28 00:00:00 2021'
>>> today.isoformat()
'2021-03-28'
>>> today.weekday()
6
>>> cal.day_name[today.weekday()]
'Sunday'
>>> today.day, today.month, today.year
(28, 3, 2021)
>>> today.timetuple()
time.struct_time(
    tm_year=2021, tm_mon=3, tm_mday=28,
    tm_hour=0, tm_min=0, tm_sec=0,
    tm_wday=6, tm_yday=87, tm_isdst=-1
)

# time
>>> time.ctime()
'Sun Mar 28 15:23:17 2021'
>>> time.daylight
1
>>> time.gmtime()
time.struct_time(
    tm_year=2021, tm_mon=3, tm_mday=28,
    tm_hour=14, tm_min=23, tm_sec=34,
    tm_wday=6, tm_yday=87, tm_isdst=0
)
>>> time.gmtime(0)
time.struct_time(
    tm_year=1970, tm_mon=1, tm_mday=1,
    tm_hour=0, tm_min=0, tm_sec=0,
    tm_wday=3, tm_yday=1, tm_isdst=0
)
>>> time.localtime()
time.struct_time(
    tm_year=2021, tm_mon=3, tm_mday=28,
    tm_hour=15, tm_min=23, tm_sec=50,
    tm_wday=6, tm_yday=87, tm_isdst=1
)
>>> time.time()
1616941458.149149


# datetime, timezones and tiemdeltas
>>> now = datetime.now()
>>> utcnow = datetime.utcnow()
>>> now
datetime.datetime(2021, 3, 28, 15, 25, 16, 258274)
>>> utcnow
datetime.datetime(2021, 3, 28, 14, 25, 22, 918195)
>>> now.date()
datetime.date(2021, 3, 28)
>>> now.day, now.month, now.year
(28, 3, 2021)
>>> now.date() == date.today()
True
>>> now.time()
datetime.time(15, 25, 16, 258274)
>>> now.hour, now.minute, now.second, now.microsecond
(15, 25, 16, 258274)
>>> now.ctime()
'Sun Mar 28 15:25:16 2021'
>>> now.isoformat()
'2021-03-28T15:25:16.258274'
>>> now.timetuple()
time.struct_time(
    tm_year=2021, tm_mon=3, tm_mday=28,
    tm_hour=15, tm_min=25, tm_sec=16,
    tm_wday=6, tm_yday=87, tm_isdst=-1
)
>>> now.tzinfo
>>> utcnow.tzinfo
>>> now.weekday()
6
>>> f_bday = datetime(
    1975, 12, 29, 12, 50, tzinfo=ZoneInfo('Europe/Rome')
)
>>> h_bday = datetime(
    1981, 10, 7, 15, 30, 50, tzinfo=timezone(timedelta(hours=2))
)
>>> diff = h_bday - f_bday
>>> type(diff)
<class 'datetime.timedelta'>
>>> diff.days
2109
>>> diff.total_seconds()
182223650.0
>>> today + timedelta(days=49)
datetime.date(2021, 5, 16)
>>> now + timedelta(weeks=7)
datetime.datetime(2021, 5, 16, 15, 25, 16, 258274)


# parsing (stdlib)
>>> datetime.fromisoformat('1977-11-24T19:30:13+01:00')
datetime.datetime(
    1977, 11, 24, 19, 30, 13,
    tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))
)

>>> datetime.fromtimestamp(time.time())
datetime.datetime(2021, 3, 28, 15, 42, 2, 142696)

>>> datetime.now()
datetime.datetime(2021, 3, 28, 15, 42, 1, 120094)


# arrow small demo
>>> import arrow
>>> arrow.utcnow()
<Arrow [2021-03-28T14:43:20.017213+00:00]>
>>> arrow.now()
<Arrow [2021-03-28T15:43:39.370099+01:00]>

>>> local = arrow.now('Europe/Rome')
>>> local
<Arrow [2021-03-28T16:59:14.093960+02:00]>
>>> local.to('utc')
<Arrow [2021-03-28T14:59:14.093960+00:00]>
>>> local.to('Europe/Moscow')
<Arrow [2021-03-28T17:59:14.093960+03:00]>
>>> local.to('Asia/Tokyo')
<Arrow [2021-03-28T23:59:14.093960+09:00]>
>>> local.datetime
datetime.datetime(
    2021, 3, 28, 16, 59, 14, 93960,
    tzinfo=tzfile('/usr/share/zoneinfo/Europe/Rome')
)
>>> local.isoformat()
'2021-03-28T16:59:14.093960+02:00'
