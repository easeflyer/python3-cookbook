#!/usr/bin/env python________
# -*- encoding: utf-8 -*-
"""
Topic: 去除字符串中多余字符
Desc : 

知识点：
    1 通过 str.strip(字符) 去除字符串两端的多余字符。
"""
import re


def strip_str():
    s = ' hello world \n'
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())

    # Character stripping
    t = '-----hello====='
    print(t.lstrip('-'))
    print(t.strip('-='))

    # 对中间不会影响
    s = ' hello     world \n'
    print(s.strip())

    print(s.replace(' ', ''))
    print(re.sub('\s+', ' ', s))

    # 生成器表达式，和面有一些需要删除的字符_________
    # 可以看到下划线被去掉了。
    # strip('_\n')  _\n 代表结尾字符可以是 _ 也可以是 \n
    with open('p11_strip.py') as f:
        lines = (line.strip('_\n') for line in f)
        for line in lines:
            print(line)


if __name__ == '__main__':
    strip_str()

