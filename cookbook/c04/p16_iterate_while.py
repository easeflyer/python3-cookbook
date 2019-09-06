#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 使用迭代器重写while无限循环
Desc : 

知识点：
    1 用迭代器 实现了 while 循环的功能。代码比较优雅可读性好。
    2 iter() 的使用。

iter() 如果包含两个参数则：当以这种方式使用的时候，它会创建一个迭代器，这个迭代器会
不断调用 callable 对象直到返回值和标记值相等为止。

"""
import sys


def process_data():
    print(data)


def reader(s, size):
    while True:
        data = s.recv(size)
        if data == b'':
            break
            # process_data(data)


def reader2(s, size):
    for data in iter(lambda: s.recv(size), b''):
        process_data(data)


def iterate_while():
    CHUNKSIZE = 8192
    with open('/etc/passwd') as f:
        for chunk in iter(lambda: f.read(10), ''):
            n = sys.stdout.write(chunk)


if __name__ == '__main__':
    iterate_while()
