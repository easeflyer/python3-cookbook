#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 转换并聚集函数
Desc : 

知识点：
    1 生成器表达式参数：sum(x * x for x in nums)，
    2 sum, min, max 参数都可以是一个 生成器，或者生成器表达式。
    3 any(iter) 参数也可以是一个 生成器，或者生成器表达式。

    4 ','.join(iter) join 也可以接受一个生成器，转换为字符串。

分析：
    使用生成器表达式作为参数。一是语法更加优雅，不需要多增加（），同时少了步骤
    计算效率也更高，节省内存空间。


"""
import os
from operator import itemgetter


def trans_reduce():
    nums = [1, 2, 3, 4, 5]
    s = sum(x * x for x in nums)
    print(s)

    files = os.listdir('./')
    #g1 = (name.endswith('.py') for name in files)
    if any(name.endswith('.py') for name in files):
        print('There be python!')
    else:
        print('Sorry, no python.')


    # Output a tuple as CSV
    s = ('ACME', 50, 123.45)
    print(','.join(str(x) for x in s))
    # Data reduction across fields of a data structure
    portfolio = [
        {'name':'GOOG', 'shares': 50},
        {'name':'YHOO', 'shares': 75},
        {'name':'AOL', 'shares': 20},
        {'name':'SCOX', 'shares': 65}
    ]
    min_shares = min(s['shares'] for s in portfolio)
    # Original: Returns 20
    min_shares = min(s['shares'] for s in portfolio)
    print(min_shares)
    # Alternative: Returns {'name': 'AOL', 'shares': 20}
    #min_shares = min(portfolio, key=lambda s: s['shares'])
    min_shares = min(portfolio, key=itemgetter('shares'))
    print(min_shares)

if __name__ == '__main__':
    trans_reduce()

