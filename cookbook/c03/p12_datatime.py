#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 日期时间转换
Desc : 

知识点：
    1 使用 timedelta 可以对时间日期进行计算。不需要考虑进制问题。闰年也会自动处理。
    2 datetime 可以处理基本的日期时间处理，间隔处理。 
    3 如果你需要执行更加复杂的日期操作，比如处理时区，模糊时间范围，节假日计算等等， 
    可以考虑使用 dateutil模块
"""
from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta



def date_time():
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print(c.days)
    print(c.seconds)
    print(c.seconds / 3600)
    print(c.total_seconds() / 3600)

    # 具体的日期
    a = datetime(2012, 9, 23)
    print(a + timedelta(days=10))
    b = datetime(2012, 12, 21)
    d = b - a
    print(d.days)
    now = datetime.today()
    print(now)
    print(now + timedelta(minutes=10))

    # 标准库中datetime模块
    a = datetime(2012, 9, 23)
    # a + timedelta(months=1)  # 这个会报错 不支持 months

    # 使用dateutil模块解决这个问题  dateutil 可以支持
    print(a + relativedelta(months=+1))
    print(a + relativedelta(months=+4))

    # Time between two dates
    b = datetime(2012, 12, 21)
    d = b - a
    print(d)
    d = relativedelta(b, a)
    print(d)
    print(d.months, d.days)



if __name__ == '__main__':
    date_time()

