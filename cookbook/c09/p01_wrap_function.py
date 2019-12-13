#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 包装函数
Desc : 

知识点：
    1 装饰器的基本用法。wraps  的使用。
    2 注意 wraps 使用与否的区别。
    3 正确的暴露 参数签名信息。
    4 假设装饰器是通过 @wraps (参考 9.2 小节) 来实现的，那么你可以通过访问
        __wrapped__ 属性来访问原始函数

2 如果不是用 wraps 则函数的__name__ 将被wrapper 取代。因为实际上 是这样的：
countdown = timethis(countdown)  timethis 返回的是 wrapper 的引用。
因此 countdown 也就是 wrapper 的引用。这个问题使用 @wraps 可以解决。当然如果你的
业务逻辑并不关注这个问题，也可以不用 @wraps

3 如果不使用 @wraps 则参数变为了 (*args,**kwargs) 这对于使用者可能造成疑惑。
因为本来我的函数只有一个参数 n


"""

import time
from functools import wraps


def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    """
    Counts down
    """
    while n > 0:
        n -= 1
def test1():
    countdown(100000)
    countdown(10000000)
    print('countdown.__name__:',countdown.__name__)
    print('countdown.__doc__:',countdown.__doc__)
    from inspect import signature
    print(signature(countdown))


def timethis1(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis1
def countdown1(n):
    """
    Counts down
    """
    while n > 0:
        n -= 1

def test2():
    countdown1(100000)
    countdown1(10000000)
    print('countdown1.__name__:',countdown1.__name__)
    print('countdown1.__doc__:',countdown1.__doc__)
    from inspect import signature
    print(signature(countdown1))


test1()
test2()