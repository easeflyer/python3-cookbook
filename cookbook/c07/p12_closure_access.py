#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 闭包访问函数内部变量
Desc : 这个使用方式 非常类似于 js

知识点：
    1 给 函数添加属性，以访问 闭包变量。见 sample()。
    2 函数 替代类：用函数替代简单的类功能 sample()
    3 sys._getframe()
    4 用 函数 闭包解决类问题。


sys._getframe()
从调用堆栈中返回一个frame对象。如果给定了可选整数深度，则返回堆栈顶部以下多次调用
的frame对象。如果它比调用堆栈更深，则会引发ValueError。depth的默认值为零，返回
调用堆栈顶部的帧。

参数是调用深度。


"""


def sample():
    '''
    n 为 sample 的局部变量。
    给 func 添加了两个属性：func.get_n = get_n, func.set_n = set_n
    func 被返回。 func 两个属性都可以访问 n。
    因此 被返回的 func 就拥有了私有属性 n 以及两个方法可以访问 n
    
    '''
    n = 0
    # Closure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func

def test1():
    f = sample()
    f()
    f.set_n(10)
    f()

import sys
class ClosureInstance:
    '''
    闭包实例解析：
        __init__ 把调用者 Stack() 的本地变量保存到 locals
        然后再把所有的 callable 更新到 __dict__ 也就是变成 本对象的方法。
        定义 __len__ 就是调用 Stack的 __len__

        总结：ClosureInstance 就是把调用者的方法变成本地方法。同时这些方法因为是
        从调用者更新过来的，又能访问 Stack()的 items 变量。(闭包特性)
    '''
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
            # print(locals) {push,pop,__len__,items}

        # Update instance dictionary with callables
        self.__dict__.update((key,value) for key, value in locals.items()
                            if callable(value) )
        # print(self.__dict__) # 只把方法放进去了。
    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()

# Example use
def Stack():
    items = []
    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


class c1:
    '''
    通过 __dict__  给类增加属性。
    '''
    v1 = 1
    v2 = 2
    def f1(self):
        pass

    def f2(self):
        return 'f2'
    def __init__(self):
        self.__dict__.update([('v3',3),])
        self.__dict__['f3'] = self.f2



def test2():
    s = Stack()
    print(s)
    s.push(10)
    s.push(20)
    print(len(s))
    print(s.pop())
    print(s.pop())


def test3():
    '''
    '''
    v1 = 1
    v2 = 2

    print(sys._getframe().f_code.co_filename)   # 当前文件名，可以通过__file__获得
    print(__file__)
    print(sys._getframe(0).f_code.co_name)      # 当前函数名
    print(sys._getframe(1).f_code.co_name)      # 调用该函数的函数的名字，如果没有被调用，则返回<module>，貌似call stack的栈低
    print(sys._getframe().f_lineno)             # 当前行号
    print(sys._getframe().f_locals)             # 返回 当前 调用堆栈，也就是test3 局部变量。
    print(sys._getframe(1).f_locals)            # 返回调用者 也就是上以帧 test4 的局部变量。


    # 通过 __dict__ 给类添加属性和方法。
    c = c1()
    print(c.v1, c.v2,c.v3,c.f3())

def test4():
    v3 = 3
    v4 = 4
    test3()

if __name__ == '__main__':
    # test1()
    # test2()
    test4()