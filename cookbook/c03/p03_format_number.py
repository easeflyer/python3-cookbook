#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 格式化输出数字
Desc : 

知识点：
    1 format() 函数的用法。 对齐，居中，小数位等。
    2 数字每三位加逗号。
"""


def format_number():
    x = 1234.56789
    # Two decimal places of accuracy
    print(format(x, '0.2f'))

    # Right justified in 10 chars, one-digit accuracy
    print(format(x, '>10.1f'))

    # Left justified
    print(format(x, '<10.1f'))

    # Centered
    print(format(x, '^10.1f'))

    # Inclusion of thousands separator
    print(format(x, ','))
    print(format(x, '0,.1f'))

    print(format(x, 'e'))
    print("0.2E:",format(x, '0.2E'))

    # strings
    print('The value is {:0,.2f}'.format(x))

    print(format(x, '0.1f'))
    print(format(-x, '0.1f'))

    swap_separators = {ord('.'): ',', ord(','): '.'}
    swap_separators = str.maketrans({'.':',',',':'.'})
    print(format(x, ',').translate(swap_separators))


if __name__ == '__main__':
    format_number()


