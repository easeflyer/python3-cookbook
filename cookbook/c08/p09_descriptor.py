#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 通过描述器定义新的实例属性
Desc : 

描述符定义：
    1 __get__() 、 __set__() 和 __delete__() 定义这三个特殊的方法。这些方法接受一个实
例作为输入，之后相应的操作实例底层的字典。def __get__(self, instance, cls):
nstance.__dict__[self.name]。
    2 接收使用描述符的对象实例instance，以及此实例的类对象cls，作为参数。

使用描述符：
    1 为了使用一个描述器，需将这个描述器的实例作为类属性放到一个类的定义中。例
    如：
    class Point:
        x = Integer('x')    # 描述符
        y = Integer('y')    # 描述符
        def __init__(self, x, y):
            self.x = x      # 同名，因此这里按规则是对描述符的赋值。
            self.y = y      # 同名，因此如上替代实力属性




test2()案例说明：
    1 Typed 定义了一个描述器。
        用途：用作属性类型检查。赋值的时候，检查是否为预期的类型。
    2 typeassert(**kwargs) 是一个装饰器。他的作用需要仔细看：
        1）他装饰的是一个类cls
        2）他接收若干个数关键字参数。
        3）他对 cls 类对象添加了。若干属性（描述器属性），然后返回 cls
            注意实例化 cls 实际上就是实例化增加属性之后的 cls
    3 Stock类被typeassert装饰，给类增加了 name,shares,price 三个描述符属性
        类的内部__init__ 定了实例化时，给三个描述符属性初始值。


总结描述符的理解：
    通过 Typed 描述符分析：我们看到 Typed 描述符类，记录了：属性名，和类型。
    然后Stock的实例，对描述符属性赋值的时候，调用了描述符的 __set__方法，此方法
    内部对value 和 属性的预期类型expected_type 进行了比较。(isinstance()) 如果
    符合类型，对实例属性进行赋值。不符合则报错。




描述符定义：
    1   一个描述符是一个有“绑定行为”的对象属性(object attribute)，它的访问控制会被描述器
        协议方法重写。
        （如上例 Typed 描述符，给Stock实例对象的name,shares,price属性。绑定了类型检查的行为，
        这三个属性的访问控制（读取和赋值）被描述器的 __get__,__set__ 重写。）

    2   任何定义了 __get__, __set__ 或者 __delete__ 任一方法的类称为描述符类，其实例对象
        便是一个描述符，这些方法称为描述符协议。
    3   当对一个实例属性进行访问时，Python 会按 
        obj.__dict__ → type(obj).__dict__ → type(obj)的父类.__dict__ 顺序进行查找，
        如果查找到目标属性并发现是一个描述符，Python 会调用描述符协议来改变默认的控制行为。
    4   描述符是 @property@classmethod@staticmethod 和 super 的底层实现机制。




参考文档：
https://www.cnblogs.com/Jimmy1988/p/6808237.html
"""

# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print('__get__:')
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('__set__:')
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        print('---1---')
        self.x = x
        print('---2---')
        self.y = y


def test1():
    p = Point(2, 3)
    print(p.x)
    p.y = 5    


# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        print('Typed.__get__:')
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls

    return decorate


# Example use
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

def test2():
    import pdb;pdb.set_trace()
    s1 = Stock("腾讯",20,98.8)
    print(s1)
    print(s1)
    print(s1)


if __name__ == '__main__':
    test2()