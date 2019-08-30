#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Topic: 序列元素过滤,筛选
Desc :

知识点：
    1 利用列表推导式提交过滤数据。
    2 利用() 返回生成器，节省内存。
    3 filter(function, iterable) 过滤。

    4 注意 test1() 列表推导式的使用。l1 用于过滤。 l2 则用于替换。
    5 itertools.compress(data, selectors): compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F

filter(function, iterable) 针对每一个 iterable 元素，执行function 返回true 的保留。
返回筛选后的结果，也是一个生成器。

"""
from itertools import compress

def test1():
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    l1 = [n for n in mylist if n>0]
    l2 = [n if n>0 else None for n in mylist]
    c1 = [n>0 for n in mylist]
    l3 = compress(mylist, c1)   # 注意 l3 返回的是迭代器。
    print("l1:",l1)
    print("l2:",l2)
    print("l3:",list(l3))

def compress1():
    mask = "110110"
    l1 = [int(n) for n in mask]
    c1 = compress('abcdef',l1)
    print(list(c1))                         # ['a', 'b', 'd', 'e']


def cb_filter():
    # 1)
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    print([n for n in mylist if n > 0])     # 筛选出 > 0
    print([n for n in mylist if n < 0])     # 筛选出 < 0 

    pos = (n for n in mylist if n > 0)      # 节省内存 返回生成器
    print(pos)
    for x in pos:                           # 迭代 输出结果
        print(x, end=',')
    print()


    # 2)
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    def is_int(val):
        try:
            x = int(val)
            return True
        except ValueError:
            return False
    ivals = list(filter(is_int, values))    # 利用 is_int 函数过滤列表
    print(ivals)
    # Outputs ['1', '2', '-3', '4', '5']

    # 3)
    # 条件过滤
    clip_neg = [n if n > 0 else 0 for n in mylist]
    print(clip_neg)


    # 4)
    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
    more5 = [n > 5 for n in counts]
    print(list(compress(addresses, more5)))


if __name__ == '__main__':
    # cb_filter()
    test1()
    compress1()