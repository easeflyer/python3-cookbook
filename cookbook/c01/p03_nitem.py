#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: collections.deque演示
Desc : deque有一个maxlen参数，当append的时候，如果超过，那么最前面的就被挤出队列。

题目：搜索某个字符串，找到后输出最后5行以及包含字符串的行。也就是最后6行
知识点：
    1 collections.deque 保留有限成员，其他被挤出
    2 注意 deque 比列表操作更快。时间复杂度：O(1) O(n)
"""
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

# Example use on a file 234234   234234 
if __name__ == '__main__':
    with open(r'../../cookbook/somefile.txt') as f:
        for line, prevlines in search(f, 'Python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)



