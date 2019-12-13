#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 使用类装饰器来增强类功能
Desc : 

知识点：
    使用装饰器给类增加功能。比继承有一些优势：
    1 没有引入集成关系
    2 不用处理  super()
    3 看起来更加直观，只是函数调用的关系。

"""


def log_getattribute(cls):
    # Get the original implementation
    orig_getattribute = cls.__getattribute__

    # Make a new definition
    def new_getattribute(self, name):
        print('1getting:', name)
        return orig_getattribute(self, name)

    # Attach to the class and return
    cls.__getattribute__ = new_getattribute
    return cls


# Example use
@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass

def test1():
    a1 = A(3)
    print(a1.x)

class LoggedGetattribute:
    def __getattribute__(self, name):
        print('2getting:', name)
        return super().__getattribute__(name)
# Example:
class A1(LoggedGetattribute):
    def __init__(self,x):
        self.x = x
    def spam(self):
        pass

def test2():
    a1 = A1(4)
    print(a1.x)

test2()



