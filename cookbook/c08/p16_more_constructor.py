#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 定义类的多个构造函数
Desc : 

类方法
    @classmethod
    def func2(cls):  cls 是没有被实例化的类对象。
    类方法调用：类对象名称.类方法()

通过类方法定义了两个构造函数。默认构造函数不变。
today() 用 @classmethod 装饰，最后返回 cls() 也就是调用原来的构造方法。

"""

import time


class Date:
    """方法一：使用类方法"""
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

a = Date(2012, 12, 21) # Primary
b = Date.today() # Alternate

print(f"a.year:{a.year} b.year:{b.year}")