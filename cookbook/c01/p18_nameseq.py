#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 通过名称访问序列 
Desc : 命名元组

知识点：
    1 创建 命名元组 namedtuple，返回一个新的命名元组类型。实例化元组。
    2 可以按照命名读取数据，也可以按照下标读取。
    3 可以像元组一样：解压赋值

    4 *args, **kwargs 前者表示多个无名参数，或者表示多个关键字参数。
    5 命名元组类似数据表，某些需求中替代字典。
"""
from collections import namedtuple


def name_seq():
    Subscriber = namedtuple('Subscriber', ['addr', 'joined'])   # 创建一个命名元组类型
    sub = Subscriber('jonesy@example.com', '2012-10-19')        # 实例化一个元组。
    print(sub)
    print(sub.addr, sub.joined)                                 # 按命名读取
    print(sub[0], sub[1])                                       # 按下标读取
    print(len(sub))
    addr, joined = sub
    print(addr, joined)

# rs = [['aa', 12, 33],['bb', 8, 15]] 参数数据
# 函数接收 records 参数 计算结果 返回合计。
# 但使用下标进行编码，代码可读性差。
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

# 对上面函数的改造
# 利用 namedtuple 建立命名元组 Stock
# st = Stock(*rec) 把普通数据 解压创建命名元组。
def compute_cost2(records):
    Stock = namedtuple('SSS', ['name', 'shares', 'price'])
    total = 0.0
    for rec in records:
        st = Stock(*rec)
        total += st.shares * st.price
    s = Stock('ACME', 100, 123.45)
    # 更新命名元组
    s = s._replace(shares=75)
    print(s)
    return total


'''
通过命名元组的 _replace(key=value) 来修改元组的值。（元组不能直接修改）
本例知识点：我们可以看到 命名元组非常像对一个表的定义。
Stock1 就是表名。元组元素的命名，就是字段名。每个新实例，就是一条记录。

另外命名元组也非常像：[{},{}] 这样的字典列表，但是字典列表需要更多的内存空间
同时命名元组也更加高效。需要注意的就是 修改时只能用 _replace 来修改，不可以直接修改。

'''


Stock1 = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock1('', 0, 0.0, None, None)

# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)  #   **解压关键字参数

def default_stock():
    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    s1 = dict_to_stock(a)
    print('s1:',s1)
    s1 = s1._replace(price=150) 
    print('s1:',s1)

    b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
    print(dict_to_stock(b))

if __name__ == '__main__':
    name_seq()
    # rs = [('aa', 12, 33)]
    rs = [['aa', 12, 33]]  # 元组和序列都可以
    print('compute_cost:',compute_cost(rs))
    print('compute_cost2:',compute_cost2(rs))
    default_stock()