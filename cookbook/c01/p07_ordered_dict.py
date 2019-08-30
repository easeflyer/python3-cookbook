#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 排序字典
Desc : 

知识点：
  1 OrderedDict 有序字典，保证了字典的插入顺序。
  2 OrderedDict 内部维护着一个根据键插入顺序排序的双向链表，占用1倍内存空间。
  3 json.dumps(dict) 把 dict 变为 json str 字符串
"""

from collections import OrderedDict
import json


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4


# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])
print(json.dumps(d))

# 默认情况下 字典是无序的。但在python3开始，小型的字典输出时默认是按照添加顺序。
# 但这并不是说字典是有序的。python2 可以明显看到结果的不同。
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['2'] = 'D'
d1['1c'] = 'C'
d1['2a'] = 'D'


for k,v in d1.items():
  print(k,v)

print(json.dumps(d1))