#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: dict子集
Desc : 

知识点：
    1 通过 字典推导式，类似列表推导式
    2 通过 元组列表转换成字典。

"""

def sub_dict():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    # Make a dictionary of all prices over 200
    p1 = {key: value for key, value in prices.items() if value > 200}
    c1 = [(key,value) for key, value in prices.items() if value > 200]
    # Make a dictionary of tech stocks
    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {key: value for key, value in prices.items() if key in tech_names}
    # 首先 用 与运算取出包含的 key 然后迭代。效率比 p2 低1.6倍
    p3 = { key:prices[key] for key in prices.keys() & tech_names }
    print(p1)
    print(dict(c1))
    print(p2)
    print(p3)
    
if __name__ == '__main__':
    sub_dict()
