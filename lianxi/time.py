from datetime import datetime
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M:%S'))
print(now.strftime('%a, %b %d %H:%M:%S'))

from datetime import datetime
dt = datetime(2017,4,18,23,45)
print(dt)
ts = dt.timestamp()
print(ts)
print(datetime.fromtimestamp(ts))
print(datetime.utcfromtimestamp(ts))

from datetime import datetime,timedelta
now = datetime.now()
print(now)
print(now+timedelta(days=1,hours=10))

from datetime import datetime,timedelta,timezone
tz = timezone(timedelta(hours=8))#创建时区UTC+8:00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz)#设置为UTC+8:00
print(dt)