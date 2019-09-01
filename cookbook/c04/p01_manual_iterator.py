#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 手动遍历迭代器
Desc : 

知识点：
    1 open 返回可迭代的文件。每次迭代返回一行内容。
    2 next() 内置函数进行迭代，使用 while True 循环。 注意捕获错误。
    3 next() 可以添加第二个参数，当迭代到最后没有元素时 返回此参数作为结束信号。比如 None 
    4 iter(list) 返回一个可迭代对象。
"""


def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

def manual_iter2():
    with open('/etc/passwd') as f:
        while True:
            line = next(f,None)
            if line is None:
                break
            print(line, end='')


def test1():
    l1 = [2,3,4,5,6,7]
    i1 = iter(l1)   # 转换为可迭代对象。 其实就是调用 l1.__iter__()
    print(next(i1))


if __name__ == '__main__':
    manual_iter2()
    test1()
