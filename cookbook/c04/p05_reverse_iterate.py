#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 方向迭代
Desc : 

知识点：
    如果不实现 __reversed__ 则要把数据先转变为 列表，需要占用较多内存。
    实现了__reversed__ 后，反向迭代效率就高多了。
"""


def reverse_iterate():
    a = [1, 2, 3, 4]
    for x in reversed(a):
        print(x)

    # 两个条件：大小可知或者实现__reversed__方法，
    # 如果都不满足，先转换为list
    # Print a file backwards
    # f = open('somefile')
    # for line in reversed(list(f)):
    #     print(line, end='')

    for rr in reversed(Countdown(30)):
        print(rr)
    for rr in Countdown(30):
        print(rr)


class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


if __name__ == '__main__':
    reverse_iterate()

