#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 简化数据结构的初始化
Desc : 
    你写了很多仅仅用作数据结构的类，不想写太多烦人的 __init__() 函数
通过定义父类的 __init__ 结合 setattr() 函数，实现用下面的方式定义属性：
    _fields = ['name', 'shares', 'price']



"""
import math


class Structure1:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure1):
    _fields = ['name', 'shares', 'price']

class Point(Structure1):
    _fields = ['x', 'y']

class Circle(Structure1):
    _fields = ['radius']
    def area(self):
        return math.pi * self.radius ** 2


def test0():

    s = Stock('ACME', 50, 91.1)
    print(f"s.name:{s.name} s.shares:{s.shares} s.price:{s.price}")
    p = Point(2, 3)
    c = Circle(4.5)


class Structure2:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        # [len(args):] 这个切片 只对 关键字参数进行访问
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))
class Stock(Structure2):
    _fields = ['name', 'shares', 'price']

def test1():
    s1 = Stock('ACME1', 51, 92.1)
    print(f"s1.name:{s1.name} s1.shares:{s1.shares} s1.price:{s1.price}")
    s2 = Stock('ACME', 50, price=91.1)
    s3 = Stock('ACME', shares=50, price=91.1)
    print(f"s2.name:{s2.name} s2.shares:{s2.shares} s2.price:{s2.price}")
    # s3 = Stock('ACME', shares=50, price=91.1, aa=1)


class Structure3:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the additional arguments (if any)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))
class Stock1(Structure3):
    _fields = ['name', 'shares', 'price']

def test2():
    s1 = Stock1('ACME', 50, 91.1)
    s2 = Stock1('ACME', 50, 91.1, date='8/2/2012')
    print(f"s1.name:{s1.name} s1.shares:{s1.shares} s1.price:{s1.price}")
    print(f"s2.name:{s2.name} s2.shares:{s2.shares} s2.price:{s2.price} s2.date:{s2.date}")


class Structure4:
    # Class variable that specifies expected fields
    _fields= []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments (alternate)
        self.__dict__.update(zip(self._fields,args))



if __name__ == "__main__":
    test0()
    test1()
    test2()
