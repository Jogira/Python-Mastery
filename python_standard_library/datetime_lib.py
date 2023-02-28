from datetime import datetime, timedelta
import time


dt = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
dt_now = datetime.now()
dt_strp = datetime.strptime("2018/01/01", "%Y/%m/%d")
dt_from = datetime.fromtimestamp(time.time())
print(dt_from)

print(f"{dt.year}/{dt.month}")
print(dt_from.strftime("%Y/%m"))


duration = dt_now - dt
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total_seconds", duration.total_seconds())
