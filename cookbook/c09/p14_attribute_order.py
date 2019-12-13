#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 类定义中属性的顺序
Desc : 
"""
from collections import OrderedDict

# A set of descriptors for various types
# 定义一个描述符 Typed 。这个命名只是普通类型名而已。
class Typed:
    _expected_type = type(None)

    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError('Expected ' + str(self._expected_type))
        instance.__dict__[self._name] = value

# 继承了 Typed 因此这几个类都是描述符
class Integer(Typed):
    """
    Integer(Typed) -> Typed
    类文档
    """
    _expected_type = int


class Float(Typed):
    _expected_type = float


class String(Typed):
    _expected_type = str


# Metaclass that uses an OrderedDict for class body
# 继承 type 因此这是一个 元类
# 元类的实例就是一个 类对象。
class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(cls, clsname, bases):
        return OrderedDict()


class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ','.join(str(getattr(self, name)) for name in self._order)


# Example use
class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
def test2():
    s = Stock('GOOG',100,490.1)
    s.name
    print(s.as_csv())

test2()

# __new__ 的理解。
'''
1 早于 __init__调用
2 接收 cls 类对象。返回 self 实例对象，用于在对象实例化前做 前期处理。
3 __new__的参数除了 cls 以外，其他都是实例化时提供的。和 __init__参数一致
'''
# super() 使用
'''
python3 可以直接用 super().函数名
'''
# add by ease for __new__ speciality
# python3 开始 int 没有 可以接收参数的 __init__ 因此以下代码报错。
class PositiveInteger1(int):
    def __init__(self, value):
        super(PositiveInteger, self).__init__(self, abs(value))
        
class PositiveInteger(int):
    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))

class Cls1:
    def __new__(cls,v1,v2,v3,v4):
        print(v1,v2,v3,v4)
        return super().__new__(cls)

    def __init__(self,v1,v2,v3,v4):
        print("__init__:",v1,v2,v3,v4)



def test1():
    i = PositiveInteger(-3)
    c1 = Cls1(3,4,5,6)
    print(i)

test1()