#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 字符串中的变量
Desc : 

知识点：
    1   vars([object]) 函数返回对象object的属性和属性值的字典对象。如果省略参数则
        返回当前作用域的所有变量。类似 locals()
    2   str.format(k1=v1,k2=v2) 也可以用 str.format_map(dict) 同等。
        可以用 vars() 返回字典的功能来作为 参数。
    3   __missing__() 解决缺失键的问题。
"""
import sys

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


class SafeSub(dict):
    """防止key找不到"""
    def __missing__(self, key):
        return '{' + key + '}'

# 关于 _getframe 的使用参考书中原文。
def sub(text):
    return text.format_map(SafeSub(sys._getframe(1).f_locals))

def var_str():
    s = '{name} has {n} messages.'
    print(s.format(name='Guido', n=37))

    # vars()和format_map
    a = Info('Guido', 37)
    print(s.format_map(vars(a)))

    name = 'Lisi'  # 缺失 n 用 {n} 替代
    print(s.format_map(SafeSub(vars())))

    name = 'Guido'
    n = 37
    print(sub('Hello {name}'))
    print(sub('You have {n} messages.'))
    print(sub('Your favorite color is {color}'))
    print(f'Hello {name}')
    print(f'You have {n} messages.')
    # print(f'Your favorite color is {color}') 报错



if __name__ == '__main__':
    var_str()

