#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 迭代器和生成器切片
Desc : 

知识点：
    1 使用 itertools.islice 对生成器进行切片。


从案例中可以看到如果直接对生成器进行切片，会发生错误。因为生成器并不知道有多少个元素。
但可以使用itertools.islice 进行切片。原理是先读取，在切片。

需要注意的是，生成器切片会对生成器进行一次性的读取，消耗元素。如果连续两次进行切片，会得到不同的结果。
"""
import itertools


def count(n):
    while True:
        yield n
        n += 1


def iter_slice():
    c = count(0)
    # print(c[10:20])
    for x in itertools.islice(c, 10, 20):
        print(x)


if __name__ == '__main__':
    iter_slice()


