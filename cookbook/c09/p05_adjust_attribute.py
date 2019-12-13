#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 可调整属性的装饰器
Desc : 你想写一个装饰器来包装一个函数，并且允许用户提供参数在运行时控制装饰器
行为。

理解：
    普通的装饰器，一般只提供固定的功能。这里我们的需求是：
    通过“参数” 在“运行时” 调整装饰器的功能。（注意这个说法）

程序理解：
    1 attach_wrapper 给 obj 对象 添加一个函数属性。
    2 装饰器 有参数的装饰器 logged 。返回一个无参数的装饰器 decorate
    3 decorate 包含了一些闭包变量，并装饰 函数1）添加日志2 返回函数结果。
    4 decorate 还包含了两个内部函数，set_level 和 set_message 并且通过 @attach_wrapper
        附加给了 wrapper 函数对象（注意这个附加过程是提前发生的）。
    5 使用@logged 装饰器，也就是使用 decorate ,结果返回的是 wrapper函数（并携带了两个方法）
    6 add 的调用触发了装饰器的功能。
    7 add.set_message add.set_level 的调用，则修改了装饰器的“状态”（闭包属性）
    8 因此 add 的再次调用 收到了闭包数据的影响而发生改变。

总结：
    通过以上分析，得出：decorate 装饰器，包含了两个函数可以改变其行为。（内部状态改变了。）


装饰器的执行：
    装饰器只会在函数定义时被调用一次。这点非常重要。
    装饰器装饰了函数 A 。 函数A 执行的时候，装饰器的功能也被体现出来。看起来好像是 装饰器是在 A 执行的时候被触发的。事实上不是。
    装饰器实在 A 定义的时候执行的。改变了定义。因此 A 调用的已经不是原来的 A 。而是已经被修改过的 A
"""

from functools import wraps, partial
import logging
import time


# Utility decorator to attach a function as an attribute of obj
# 将函数附加为obj的属性
def attach_wrapper(obj, func=None):
    '''
    1 如果 func is None：那么返回已经绑定obj 的 attach_wrapper，obj没有变化。
    2 否则如果有func 参数。则把func 设置为 obj 的属性。
    '''
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    # return func


def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Attach setter functions
        # 这里使用 attach_wrapper 时只提供了 obj 参数，因此返回绑定了obj的 attach_wrapper
        # 也就是给 obj (wraper) 添加了 set_level 属性。
        # 需要特别注意的是 装饰器的执行 先于函数。因此这里 set_level 已经添加给了 wrapper
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            # nonlocal 允许函数修改外部变量
            nonlocal level
            level = newlevel
        # 给 wrapper 添加了 set_message 属性
        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper

    return decorate


# Example use
# @logged(logging.DEBUG) 就是 @decorate
@logged(logging.DEBUG)  
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

def test1():
    # import pdb;pdb.set_trace()
    logging.basicConfig(level=logging.DEBUG)
    add(2, 3)
    add.set_message('Add called')
    add(2, 3)
    add.set_level(logging.WARNING)
    add(2, 3)

    print('---------------------')
    spam()
    spam.set_message('Add called')
    spam()
    spam.set_level(logging.WARNING)
    spam()
test1()

def timethis(func):
    """
    Decorator that reports the execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@logged(logging.DEBUG)
@timethis
def countdown(n):
    while n > 0:
        n -= 1

countdown(10000000)
countdown.set_level(logging.WARNING)
countdown.set_message("Counting down to zero")
countdown(10000000)


@timethis
@logged(logging.DEBUG)
def countdown1(n):
    while n > 0:
        n -= 1

print('****************************************')
countdown1(10000000)
countdown1.set_level(logging.WARNING)
countdown1.set_message("Counting down to zero")
countdown1(10000000)