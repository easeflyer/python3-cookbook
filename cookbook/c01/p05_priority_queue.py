#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 优先级队列
Desc :  


知识点：
    1 元组的可以比较特性，如果是字典则会报错。
    2 元组中 priority  [praɪ'ɔrəti] 实现优先级，也就是第一排序条件。
    3 利用 _index 实现插入顺序，也就是第二排序条件
"""
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

if __name__ == "__main__":

    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
