#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 计算当前月份的日期范围
Desc : 

知识点：
    1 calendar.monthrange(start_date.year, start_date.month)  返回月份有多少提案
    2 date.today().replace(day=1) 把日期修改为 1号
    3 利用生成器 输出指定间隔的日期。
    4 timedelta 表示特定日期间隔。用于日期间隔计算
"""
from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


def month_range():
    a_day = timedelta(days=1)
    first_day, last_day = get_month_range()
    while first_day < last_day:
        print(first_day)
        first_day += a_day

    # 使用生成器
    for d in date_range(datetime(2012, 9, 1), datetime(2012, 10, 1),
                        timedelta(hours=6)):
        print(d)


if __name__ == '__main__':
    month_range()

    print(get_month_range(datetime(2018,2,11)))