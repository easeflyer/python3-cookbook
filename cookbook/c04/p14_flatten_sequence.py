#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""
from collections.abc import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


def flatten_seq():
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    # Produces 1 2 3 4 5 6 7 8
    print(list(flatten(items)))
    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    print(list(flatten(items)))
if __name__ == '__main__':
    flatten_seq()