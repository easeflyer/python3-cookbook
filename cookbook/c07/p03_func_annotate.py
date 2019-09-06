#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 函数注解元信息
Desc : 给函数添加帮助信息。

元信息并不会对程序执行产生任何影响。
但可以给代码提高可读性。建议添加。
"""

def add(x:int, y:int) -> int:
    return x + y

help(add)

print(add.__annotations__)
print(add('aaa','bbb'))     # 元信息并不会对程序执行产生任何影响。

