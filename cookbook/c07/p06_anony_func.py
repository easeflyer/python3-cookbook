#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 匿名函数lambda表达式
Desc : 
"""

add = lambda x, y: x + y
print(add(2,3))


'''
注意下面的例子：
x 是个普通变量。在 lambda 表达式中 x 的值，并没有被赋值。
可以尝试注释掉 x = 10。 lambda 表达式中的 x 的值是在执行的时候被赋值的。
'''

x = 10  # 即使  这里注释掉 程序也可以正常运行。
a = lambda y: x + y
x = 20
b = lambda y: x + y

print(a(10))
print(b(10))



'''
分析：
    funcs 包含了5个 匿名函数。每个匿名函数都返回了 x+n 那么n的值是多少呢？
    新手可能会认为 n 为 0-4 而结果却不是。这里包含两个重要的知识点：
    1 lambda 函数是执行的时候才调用的 n 的值。
    2 n 的值在 列表生成式中 是一个闭包。外部无法调用。但是所有的 lambda 函数可以。
'''
funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
    print(f(0))