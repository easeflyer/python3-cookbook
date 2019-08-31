#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 消除序列重复值并保持顺序
Desc : 

知识点：
    1 利用set 去除重复，并保持顺序。dedupe()
    2 对不可哈希的对象进行去重。添加了 key lambda表达式。利用表达式的结果进行比较去重。
    3 文件去重同样的道理。

注意：
    key 的实现方法。key(item)  item 是 for item in items 获得的。因此我们看到
    lambda 表达式 的参数就是被迭代对象的每个元素。如果是字典 就是 key 值。


"""


def dedupe(items):
    """元素都是hashable"""
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe2(items, key=None):
    """元素不是hashable的时候 必须给出 key
    如果元素是 hashable 则可以 key=None

    val 获得 key(item) 值，也就是通过 key(item) 来去重。
    (d['x'], d['y']))   x,y 都相同才算重复。
    d['x'])             x 重复就算重复。
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


def remove_dup():
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))
    print(set(a))           # 顺序发生变化

    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    d1 = dedupe2(a, key=lambda d: (d['x'], d['y']))
    d2 = dedupe2(a, key=lambda d: d['x'])
    print(list(d1))
    print(list(d2))

'''
文件去重：
with open(somefile,'r') as f:
    for line in dedupe(f):
    ...

f 是可迭代的，每个元素就是一行。因此和上面的列表去重同等。
'''



if __name__ == '__main__':
    remove_dup()
