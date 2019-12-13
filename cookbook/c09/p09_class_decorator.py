#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 将装饰器定义成类
Desc : 
知识点：
    1 可调用对象，只要是可以后面加()的都是可调用对象。
    2 如果在类中实现了 __call__ 方法，那么实例对象也将成为一个可调用对象，
        注意类对象本身是 callable 的，这里指的是实例对象变为 callable

    @Profiled  # Profiled 是一个类
    def add(x, y):

    3 MethodType 使用 MethodType 可以把方法绑定到类，或者实例对象上。注意如果不使用。
        方法内部无法访问 self ，以及和对象相关的一些元信息都是丢失的。
        anotherRef=types.MethodType(methodName,instance)
        把methodName（方法的） 绑定到实例instance 上，并返回方法的引用。
        举例：s1.set_age=MethodType(set_age,s1,Student)

等价于

    add = Profiled(add) # 显然 类的实例化返回的是一个实例对象。因此定义 __call__
    使得 add 即是一个实例对象，也是callable
    同时 实现了 __get__ 因此 Profiled 也是一个描述符。也就是说对于 add的读写，将会被
    __get__ 代理


分析理解：
    1 wraps(func)(self)
    普通的装饰器是这样 使用 @wraps 的：
        @wraps(func)
        def wrapper(*args, **kwargs):
    也就等价于：
        wrapper = wraps(func)(wrapper)
        且最终返回的函数是 wrapper (调用func 实际最终被调用执行的是 wrapper)
    也就是说 @functools.wraps 用来装饰 要被返回的那个函数。
    因此 wraps(func) 装饰的是 self。 Profiled 装饰的是 func， 也就是说当调用 func
    的时候，实际调用的是 Profiled 的实例。

    2 程序执行流程：
    Spam().bar(3)
    1）Spam() 实例 调用 bar 方法，参数为3
    2）bar 方法被Profiled 装饰，bar 实际上引用的是 Profiled 的实例。但
    3）Profiled 同时也是描述符，因此 对 bar() 的访问首先被__get__代理。
    4）结果是把 Profiled 的实例绑定到了 Spam()实例上。并返回self。
    5）self 本身是callable 的，因此最后执行的是 __call__ 。
    6) __wrapped__调用原方法，返回3

    详细原理见cookbook.

"""

import types
from functools import wraps

class Profiled:
    def __init__(self, func):
        print('==============0')
        wraps(func)(self)  # 注意这个语法。
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        print('==============2')
        return self.__wrapped__(*args, **kwargs) # __wrapped__ 访问原始函数

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            print('==============1')
            return types.MethodType(self, instance)
            # types.MethodType(self, instance) 返回的是一个方法的引用。
            # 把self 绑定到 instance 实力上。注意 self 是 callable
            # 1）instance 多了 self,2) bar 变为了 self,那么 bar(3) 实际调用的是
            # Profiled 实例(3) 也就是 __call__()， __wrapped__ 访问原始函数。

# Profiled 作为描述符，这里并没有起到作用。因为self 是文档本身。
@Profiled
def add(x, y):
    return x + y

# Profiled 作为描述符，这里 bar 的调用将会被代理。
class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)

add(2,3)
Spam().bar(3)



import types
from functools import wraps

def profiled(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda: ncalls
    return wrapper

# Example
@profiled
def add(x, y):
    return x + y

