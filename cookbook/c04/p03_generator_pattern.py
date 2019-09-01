#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 使用生成器创建新的迭代模式
Desc : 

知识点：
    1 生成器函数的内部规则，就是迭代结果的返回规则。
    2 只要有 yield 返回的。都是生成器。

"""


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done')


def gen_pattern():
    for n in frange(0, 4, 0.5):
        print(n)
    print(list(frange(0, 1, 0.125)))

    #生成器函数
    # Create the generator, notice no output appears
    c = countdown(3)
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))

if __name__ == '__main__':
    gen_pattern()