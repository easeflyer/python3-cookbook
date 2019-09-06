#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 只允许关键字形式的参数
Desc : 

知识点：
    1 强制关键字参数。可以提高程序的可读性。


注意 *号参数必须放在除了 **关键字参数外的最后位置。 **关键字参数只能放在最后位置。
可以看到 recv 有个 * 号参数。可以理解为“释放”了所有“位置参数。”因此 block 只能是一个关键字参数。
"""


def recv(maxsize, *, block):
    'Receives a message'
    pass

# recv(1024, True) # TypeError
recv(1024, block=True)  # Ok


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


re1 = minimum(1, 5, 2, -5, 10)  # Returns -5
re2 = minimum(1, 5, 2, -5, 10, clip=0)  # Returns 0

print(re1,re2)