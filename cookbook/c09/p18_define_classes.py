#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 以编程方式定义类
Desc : 

1 定义两个函数。 __init__(), cost()
2 定义一个字典，成员就是以上两个函数。
3 用 types.new_class() 以及以上字典，就可以通过代码实例化一个普通的“类对象”
4 注意：Stock.__module__ = __name__  也是必须的步骤，参考 cookbook 文档。
5 如果有元类，也可以通过第三个参数定义。

这里的类对象，和我们用 class 声明的类对象无异。


学习到这里暂时中止。
"""

# stock.py
# Example of making a class manually from parts

# Methods
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    '__init__': __init__,
    'cost': cost,
}

# Make a class
import types

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__

import operator
import types
import sys


def named_tuple(classname, fieldnames):
    # Populate a dictionary of field property accessors
    cls_dict = {name: property(operator.itemgetter(n))
                for n, name in enumerate(fieldnames)}

    # Make a __new__ function and add to the class dict
    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__

    # Make the class
    cls = types.new_class(classname, (tuple,), {},
                          lambda ns: ns.update(cls_dict))

    # Set the module to that of the caller
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls
