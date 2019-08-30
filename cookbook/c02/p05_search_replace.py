#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 字符串搜索和替换
Desc : 

    知识点：
        1 re.sub() 或者 正则对象.sub(), 正则替换。（注意不是查找）
        2 newtext,n re.subn()  n 返回替换的次数。
        3 month_abbr[n] 返回月份小写 list(month_abbr)
        4 用回调函数处理替换结果。回调函数接收 正则参数，返回替换结果。
        5 group(n) 调取匹配分组，也就是模式中的第几个小括号
"""
import re
from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


def search_replace():
    text = 'yeah, but no, but yeah, but no, but yeah'
    print(text.replace('yeah', 'yep'))

    # 复杂的模式，使用sub()
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

    # 先编译 再替换。
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    print(datepat.sub(r'\3-\1-\2', text))

    # 更复杂的替换，使用回调函数
    print(datepat.sub(change_date, text))

    # 同时返回替换次数
    newtext, n = datepat.subn(r'\3-\1-\2', text)
    print(newtext, n)


if __name__ == '__main__':
    search_replace()

