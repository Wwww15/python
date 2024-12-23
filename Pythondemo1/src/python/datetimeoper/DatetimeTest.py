import re
from datetimeoper import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    init_time = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    regex = r'UTC([-+\w]+)\:00'
    match = re.match(regex, tz_str)
    timezone_hour = int(match.group(1))
    utc_time = init_time.replace(tzinfo=timezone(timedelta(hours=timezone_hour)))
    return utc_time.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
