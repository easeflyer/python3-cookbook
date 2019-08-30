#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 命名切片
Desc : 利用 slice() 切片对象，对切片数字进行命名。增强了代码的可读性。

知识点：
    1 切片命名，增强可读性。避免切片数字硬编码，难于理解。
    2 slice(start,stop,step) 创建切片对象，SHARES = slice(20, 23)
    3 slice.indices(len) 对 slice 切片对象的3个参数进行调整，避免越界。
"""


def name_slice():
    record = '....................100 .......513.25 ..........'
    cost = int(record[20:23]) * float(record[31:37])

    SHARES = slice(20, 23)
    PRICE = slice(31, 37)
    cost = int(record[SHARES]) * float(record[PRICE])
    print(cost)
    print(SHARES.start)
    print(SHARES.stop)
    print(SHARES.step)

    a = slice(5, 50, 2)
    s = 'HelloWorld'
    print(a.indices(len(s)))
    for i in range(*a.indices(len(s))):
        print(s[i])


if __name__ == '__main__':
    name_slice()