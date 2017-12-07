# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    #first turn str to datetime then turn it into to_timestamp
    #the point is how to deal with time zone
    #use the string timezone to get the utc tzone number
    tz_time = int(tz_str[3:-3])
    #turn the string time to datetime and forcefully set the timezone
    # too much conversion might make the timestamp not accurate
    dt_time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone(timedelta(hours=tz_time)))

    #dt_timeUTC = dt_time - timedelta(hours = tz_time)
    #(dt_time,tz_time,dt_timeUTC,dt_time.timestamp())
    return dt_time.timestamp()

# test:

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')
