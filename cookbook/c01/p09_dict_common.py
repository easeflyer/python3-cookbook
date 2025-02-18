#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 字典的集合操作
Desc : 


知识点：
    1 dict.keys() dict.values(),items() 返回视图对象。
    2 视图对象类似 集合set。因此可以直接当做 set 来进行运算。比如并|交&差-运算

视图对象：被操作的字典变化时，视图对象也会相应改变。

"""


def dict_commonality():
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    # Find keys in common
    print(a.keys() & b.keys())  # { 'x', 'y' }
    # Find keys in a that are not in b
    print(a.keys() - b.keys())  # { 'z' }
    # Find (key,value) pairs in common
    print(a.items() & b.items())  # { ('y', 2) }

    print(type(a.items()))

    for a, b in a.items():
        print(a, b)


if __name__ == '__main__':
    dict_commonality()