#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 对象自定义格式化
Desc : 


知识点：
    1 __format__ 的使用
    2 format {:} 语法的使用。

__format__ 在执行 format() 函数，或者方法的时候，会被调用。
{:code} 定义的模板 code 会作为参数 发给 __format__ 决定对象的实际输出模板。
也就是说 {:code} 也就等于 {d.year}-{d.month}-{d.day} 的替代。
"""

class Date:
    _formats = {
        'ymd': '{d.year}-{d.month}-{d.day}',
        'mdy': '{d.month}/{d.day}/{d.year}',
        'dmy': '{d.day}/{d.month}/{d.year}'
    }

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = self._formats[code]
        return fmt.format(d=self)


d = Date(2012, 12, 21)
print(d)
print(format(d, 'mdy'))
print('The date is default:{}'.format(d))
print('The date is {:ymd}'.format(d))
print('The date is {:mdy}'.format(d))