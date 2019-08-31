#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 检查字符串开始或结尾
Desc : 

知识点：
    1 了解 re.match, re.search 的用法
    2 使用 .startswith() .endswith() 检查字符串的开头和结尾。
    3 上面两个函数可以用元组 做参数，允许多个可能的结果。

re.match(pattern, string, flags=0)   
    尝试从字符串的起始位置匹配一个模式，不是起始位置匹配则返回none。
re.search(pattern, string, flags=0)
    扫描整个字符串并返回第一个成功的匹配。

    pattern 正则： r"\d{0,3}"
    string  字符串
    flags   修饰符
参考：https://www.runoob.com/python3/python3-reg-expressions.html

"""
import re
import os
from urllib.request import urlopen


def start_end():
    filename = 'spam.txt'
    print(filename.endswith('.txt'))    # True
    print(filename.startswith('file:')) # False
    url = 'http://www.python.org'
    print(url.startswith('http:'))      # True

    filenames = os.listdir('.')
    print(filenames)                    # 文件名列表
                                        # 通过 endswith 筛选列表
    print([name for name in filenames if name.endswith(('.py', '.c'))])
                                        # any 判断是否存在 .py 文件
    print(any(name.endswith('.py') for name in filenames))

    choices = ['http:', 'ftp:']
    url = 'http://www.python.org'
    url.startswith(tuple(choices))

    # 切片实现，看上去不美
    filename = 'spam.txt'
    print('[-4:]',filename[-4:] == '.txt')      # True
    url = 'http://www.python.org'       # True
    print('or :',url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

    # 正则式实现
    url = 'http://www.python.org'       # True 正则判断
    print(re.match('http:|https:|ftp:', url))


def read_data(name):
        if name.startswith(('http:', 'https:', 'ftp:')):
            return urlopen(name).read()
        else:
            with open(name) as f:
                return f.read()

if __name__ == '__main__':
    start_end()
    content = read_data("http://www.ushow.org")
    print(content)
