#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 多值映射
Desc : 字典中的键映射多个值

问题分析：
  这里需要一个字典，字典中的元素的值 可能是列表或者集合，也就是多值。
  如果我们使用一般的构造方式，需要给字典的每个元素，初始化然后再添加值，见test1()

知识点：
  1 defaultdict 可以解决以上问题。
  2 注意初始值的处理。以及数据结构的选择。

  使用 defaultdict 构造上面的数据结构，则可以直接添加即可。
  d = defaultdict(list) 会为每个 key 自动初始化空列表。同时如果我们读取不存在的key
  也会初始化一个空列表，造成 d 数据结构增加了一个元素。


"""

from collections import defaultdict



def test1():
  d = {}
  #d['a'] = []  如果用普通数据格式，必须手动初始化每个 key 否则 append 将会报错。
  d.setdefault('a',[])
  d['a'].append(1)


def multi_dict():
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['a'].append(2)
    d['b'].append(4)
    print("list:",d)
    print("d[c]:",d['c'])

    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['a'].add(2)   # set data format can't has same value
    d['b'].add(4)
    print("set:",d)
    d = {} # A regular dictionary
    d.setdefault('a', []).append(1)
    d.setdefault('a', []).append(2)
    d.setdefault('a', []).append(2)
    d.setdefault('b', []).append(4)
    print("default:",d)


if __name__ == "__main__":
    multi_dict()
    #test1()

