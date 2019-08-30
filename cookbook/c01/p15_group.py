#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 分组迭代
Desc : 

知识点：
    1 groupby 返回 <itertools.groupby object at 0x7feddfe1f8f0> 对象
    2 list(Groupby) 返回列表(key,_groupbyer) key 分组字段， groupbyer 分组元素。
    3 用defaultdict 构建多值字典。对数据按照日期分组。

分析：
    defaultdict 速度更快，并且可以对日期进行随机访问。缺点是占用更多内存。
    groupby 的好处是用于分组输出，占用更少内存。

"""
from operator import itemgetter
from itertools import groupby


def group_iter():
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

    # Sort by the desired field first
    rows.sort(key=itemgetter('date'))
    print(groupby(rows, key=itemgetter('date')))
    print(list(groupby(rows, key=itemgetter('date'))))
    # Iterate in groups
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(' ', i)

    # defaultdict使用 
    # 这里构造的是一个 多值 字典。日期是键，所有的记录是值。
    from collections import defaultdict
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)

if __name__ == '__main__':
    group_iter()