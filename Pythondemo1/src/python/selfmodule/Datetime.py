from datetime import datetime, timedelta

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

add_time =  now + timedelta(hours=1)
print(add_time)

decrease_time = now - timedelta(minutes=30)
print(decrease_time)

