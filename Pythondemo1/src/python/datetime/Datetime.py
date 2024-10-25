from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)

print(type(now))

day = datetime(2020, 9, 12, 20, 15)
print(day)

day_timestamp = day.timestamp()
print(day_timestamp)

now_timestamp = now.timestamp()
print(now_timestamp)

now_new_day = datetime.fromtimestamp(now_timestamp)
print(now_new_day)
now_utc_day = datetime.utcfromtimestamp(now_timestamp)
print(now_utc_day)

date = datetime.strptime("2024-04-12 12:19:30", "%Y-%m-%d %H:%M:%S")
print(date)

now_str = now.strftime("%Y-%m-%d %H:%M:%S")
print(now_str)

add_time = now + timedelta(hours=1)
print(add_time)

decrease_time = now - timedelta(minutes=30)
print(decrease_time)

time_utc_zone = timezone(timedelta(hours=8))
# 强制设置一个时区
utc_time = now.replace(tzinfo=time_utc_zone)
print(utc_time)

# 初始化时间时，设置时区
init_utc_date = datetime(2020, 9, 12, 20, 15, tzinfo=time_utc_zone)
print(init_utc_date)

utc_now = datetime.now(timezone.utc)
print(utc_now)

# 转换为北京时间
peking_time = utc_now.astimezone(timezone(timedelta(hours=8)))
print(peking_time)

# 转换为东京时间
tokyo_time = utc_time.astimezone(timezone(timedelta(hours=9)))
print(tokyo_time)

# 北京时间转换为东京时间
tokyo_time_two = peking_time.astimezone(timezone(timedelta(hours=9)))
print(tokyo_time_two)
