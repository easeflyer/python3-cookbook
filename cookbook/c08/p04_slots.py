#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 使用slots来减少内存占用
Desc : 

知识点：
    1 使用 __slots__ 节约内存。
    2 限制了能使用的属性。

当你定义 __slots__ 后， Python 就会为实例使用一种更加紧凑的内部表示。实
例通过一个很小的固定大小的数组来构建，而不是为每个实例定义一个字典，这跟元
组或列表很类似。在 __slots__ 中列出的属性名在内部被映射到这个数组的指定小标
上。使用 slots 一个不好的地方就是我们不能再给实例添加新的属性了，只能使用在
__slots__ 中定义的那些属性名。

使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：
继承子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。
"""


class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

