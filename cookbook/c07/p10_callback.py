#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 带状态值的回调函数
Desc : 回调函数 需要保存额外的状态值。

知识点：
    1 使用三种方法实现 带有状态值的回调函数
    2 对三种方法进行比较分析

方法1：用类的方法做回调函数。那么累的属性就是状态值。随实例化后保持可被回调函数访问。

方法2：使用闭包，给函数提供环境变量。
方法3：使用协程，也就是用 yeild 返回。因为 yield 既可以返回结果，也可以通过send 传递
数据，因此和调用函数的过程非常类似。

"""


def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


def add(x, y):
    return x + y


# 类方案
class ResultHandler:

    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ('hello', 'world'), callback=r.handler)


# 闭包方案
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

handler = make_handler()
apply_async(add, (2, 3), callback=handler)
apply_async(add, ('hello', 'world'), callback=handler)


# 协程方案
def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))



handler = make_handler()
next(handler) # Advance to the yield
apply_async(add, (2, 3), callback=handler.send)
apply_async(add, ('hello', 'world'), callback=handler.send)


def test1():
    '''
    这是一个闭包的例子。
    可以看到 func1 一直携带了 state 这个状态变量。并且作为自己的私有变量使用。
    知识点：1 闭包 2 
    '''
    def func():
        state = 0
        def func1(a=None):
            nonlocal state
            if a is not None:
                state += a
            else:
                print("a:",state)
        return func1

    f1 = func()

    f1()
    f1(2)
    f1()
    f1(3)
    f1()
print('-------------------------------test1--------------------')
test1()
