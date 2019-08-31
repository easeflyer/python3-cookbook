#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: collections.deque演示
Desc : deque有一个maxlen参数，当append的时候，如果超过，那么最前面的就被挤出队列。

题目：保留最后有限几个元素的历史记录
知识点：
    1 通过 open 打开纯文本文件。可以对文件进行迭代，每次获得一行。
    2 list(open(filename)) 可以吧文件以行的形式保存成 list 
    3 collections.deque 保留有限成员，其他被挤出
    4 注意 deque 比列表操作更快。时间复杂度：O(1) O(n)
"""
from collections import deque


def search(lines, pattern, history=5):
    '''
    输入：
        lines           就是 文本文件对象。
        pattern         是匹配模式
        history         仅保留5条记录
    返回：
        li              一行文本
        previous_lines  保存在队列里的行
    '''
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

def test1():
    with open(r'../../cookbook/somefile.txt') as f:
        for line, prevlines in search(f, 'Python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)


def test0():
    with open(r'../../cookbook/somefile.txt') as f:
        for line in f:
            print(line,end="")

    filelist = list(open(r'../../cookbook/somefile.txt'))
    print(filelist)

# Example use on a file
if __name__ == '__main__':
    test1()

