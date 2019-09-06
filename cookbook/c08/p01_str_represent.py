#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 实例的字符串显示
Desc : 

__repr__
    1 对象的代码表示形式
    2 交互解释器中直接打这个对象的输出一致
__str__
    print(对象) 的默认输出
    如果 __str__() 没有被定义，那么就会使用 __repr__() 来代替输出。

{0.x!r} 意思是 输出 第0个参数的x属性，并且用 __repr__来提供输出
"""


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3, 4)
print("This is Pari:{!r}".format(p))    # __repr__ 输出
print("This is Pari:{}".format(p))      # 默认__str__ 输出

'''
repr(p)     Pair(3,4)

eval(repr(p)) 等于 eval('Pair(3,4)') 也就等于 p

'''