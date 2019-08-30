#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 排序dict列表
Desc : 

知识点：
    1 sorted 的使用。对 dict 排序。 key 参数是一个  callable
    2 key(callable) 可以用 itemgetter 来创建。也可以用 lambda 创建。
    3 用 itemgetter 比 lambda 效率高一些。

    这是对 dict 进行排序，如果对 普通对象呢？ 参考下节。
"""

from operator import itemgetter
from pprint import pprint
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


def sort_dictlist():

    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    rows_by_lname = sorted(rows, key=lambda x:x['lname'])
    pprint(rows_by_fname)
    pprint(rows_by_uid)
    pprint(rows_by_lname)

    rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
    pprint(rows_by_lfname)

if __name__ == '__main__':
    sort_dictlist()
