#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 带外部状态的生成器
Desc : 

知识点：
    1 enumerate 的使用。
    2 通过定义一个类，并实现__iter__。 不但能使用自定义的迭代器规则，同事还可以访问相关属性。

a = ['aa','bb','cc']
list( enumerate(a,1)) [(1, 'aa'), (2, 'bb'), (3, 'cc')]  1 设定起始数值
"""
from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


def gen_extrastate():
    with open('p06_generator_extrastate.py') as f:
        lines = linehistory(f)
        for line in lines:
            if 'python' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')


if __name__ == '__main__':
    gen_extrastate()


