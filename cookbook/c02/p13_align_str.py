#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 对齐字符串
Desc : 

知识点：
    1 ljust, rjust, center
    2 对齐，用特定字符填充空白。
    3 

以下两种方式是同等的作用：
    print(format(text, '>20'))
    print('{:>20s}'.format(text))
    其中{:} 是固定的格式， s 代表字符。

参考：
    https://docs.python.org/zh-cn/3/library/string.html#formatspec
    https://www.runoob.com/python/att-string-format.html


"""


def align_str():
    text = 'Hello World'
    print(text.ljust(20))       # 'Hello World         '
    print(text.rjust(20))       # '         Hello World'
    print(text.center(20))      # '    Hello World     '

    # 填充字符
    print(text.rjust(20,'='))   # '=========Hello World'
    print(text.center(20,'*'))  # '****Hello World*****'

    # format函数
    print('-----------------------------------format------------')
    print(format(text, '>20'))  # 右对齐
    print(format(text, '<20'))  # 左对齐
    print(format(text, '^20'))  # 居中
    # 同时增加填充字符
    print(format(text, '=>20')) # 右对齐 = 填充
    print(format(text, '*^20')) # 居中 * 填充

    # 格式化多个值
    print('{:=>10s} {:*^10s}'.format('Hello', 'World'))

    # 格式化数字
    x = 1.2345
    print(format(x, '=^10.2f'))


if __name__ == '__main__':
    align_str()

