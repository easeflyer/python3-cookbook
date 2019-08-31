#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 合并多个字典或映射
Desc : 

知识点：
    1 使用 ChainMap “合并”了两个字典。
    2 用途：查找值，检查某些键是否存在。

ChainMap：
    1 并没有建立新的字典。
    2 两个字典的重复键，第一个字典值被返回。
    3 修改新建更新，都会影响第一个字典。

"""

from collections import ChainMap

def combine_map():
    a = {'x': 1, 'z': 3 }
    b = {'y': 2, 'z': 4 }
    c = ChainMap(a,b)
    print('c[x]:',c['x']) # Outputs 1 (from a)
    print('c[y]:',c['y']) # Outputs 2 (from b)
    print('c[z]:',c['z']) # Outputs 3 (from a)

    print("len(c):",len(c))
    print("c.keys:",list(c.keys()))
    print("c.values:",list(c.values()))

    c['z'] = 10
    c['w'] = 40
    print('c[y]:',c['y'])
    c['y'] = 20             # b 仍然不会被修改，而是给 a 增加了 y
    print('c[y]:',c['y'])
    del c['x']
    print("a:",a)
    print("b:",b)
    del c['y']
    print('...del c[y]...')
    print("a:",a)
    print("b:",b)

    print('-----------------------------ChainMap opt------------')
    values = ChainMap()
    values['x'] = 1
    # Add a new mapping
    values = values.new_child()
    values['x'] = 2
    # Add a new mapping
    values = values.new_child()
    values['x'] = 3
    print(values)
    print(values['x'])
    # Discard last mapping
    values = values.parents
    print(values['x'])
    # Discard last mapping
    values = values.parents
    print(values['x'])
    print(values)


# update 需要另外创建一个字典。
# update(a) 用 a 字典的值更新 merged 字典 a 字典不变，merged 相同键被更新。
def update1():
    a = {'x': 1, 'z': 3 }
    b = {'y': 2, 'z': 4 }
    merged = dict(b)
    merged.update(a)
    print("merged:",merged)     # {'y': 2, 'z': 3, 'x': 1}
    print("a:",a)               # {'x': 1, 'z': 3 }
    print("b:",b)               # {'y': 2, 'z': 4 }


if __name__ == '__main__':
    #combine_map()
    update1()