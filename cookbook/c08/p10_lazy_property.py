#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 延迟属性 （描述符的应用）
Desc : 

解析：

    1 lazyproperty 类定义了描述符。且仅仅定义了 __get__， 我们知道。描述符，就是对
实例属性的代理。用作对使用他的对象，代理属性的访问。也就是说这些属性的访问，被描述符
的 __get__,__set__ 方法截获处理。

    2 __get__ 方法，代理了读取访问。也就是c.area 的读取
    if instance is None:   # 如果通过 Cirle.area() 的方式访问属性，则 instance is None
        return self

    value = self.func(instance) 
        self.func 实际上就是被描述符（同时也是装饰器）装饰的area属性（方法）。
        lazyproperty 的构造方法 __init__(self,func) 接收到area 并保存起来 。
        self.func(instance) 其实就是 执行 area(self) 一样的效果。计算获得结果value
        setattr(instance, self.func.__name__, value)
        给 instance 也就是Circle 的实例，添加属性 area = value
        第二次访问的时候因为是 非数据描述符，因此晚于 实例描述符。因此从新建的实例描述符读取。

    setattr(instance, self.func.__name__, value)
    return value

    3 Class Circle
        @lazyproperty
        def area(self):
        根据装饰器的概念。以上定义就相当于。
        area = lazyproperty(area) 
        从语法上可以看出来。lazyproperty 即是装饰器又是描述符。因此
        area 变成了 描述符属性。也就是对于 实例.area 的访问被代理。
    

func1(func2())
func1(func2)()

"""
import math


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value
    # def __set__(self,instance,value):     # 如果我们增加了 __set__ 变为数据描述符。
    #     pass                              # 因此造成每次对 c.area 的读取都被代理。失去了意义。

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius

def lazyproperty2(func):
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy

def test1():
    c = Circle(4.0)
    print("1):",vars(c))  # {'radius': 4.0}
    print("2):",c.area)
    print("3):",vars(c))  # {'radius': 4.0, 'area': 50.26548245743669}
    print("22):",c.area)
#    del c.area
    print("4):",vars(c))  # {'radius': 4.0}
    print("5):",c.area)

# ------------------------------------------------------
# 装饰器 Decorator
# 首先要明确，装饰器是对 func 也就是被装饰的函数的处理。而不是对 func() 的结果做处理。
# 对 func 的代理，而不是对结果再处理。
# fun = jisuan(fun)  的语法糖
def deco1(func):
    def wrapper(*args):   # args 是 被装饰函数的参数
        print('wrapper')
        re = func(*args)
        print(re)
    return wrapper
        

class Test1:
    @deco1
    def func1(self):
        return 3


def test2():
    t1 = Test1()
    t1.func1()



if __name__ == '__main__':
    test1()
    #test2()