#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 可管理的属性
Desc : 

知识点：
    1 @property，@first_name.setter，@first_name.deleter   属性定义。
    2 __init__ 也可以调用属性 setter
    3 property 属性定义在了方法里，因此可以进行类型检查，或其他逻辑。
    4 property 属性，其实在 类而不是实例 内部有实现为 property.fget,fset,fdel
    5 property 因为是方法实现的。因此可以作为动态属性，只有被调用的时候才计算

fget,fset,fdel
一个 property 属性其实就是一系列相关绑定方法的集合。如果你去查看拥有
property 的类，就会发现 property 本身的 fget、 fset 和 fdel 属性就是类里面的普通方
法。
可以理解为：当使用这个装饰器的时候。就等于定义了。 类.属性名.fget,fset,fdel


1 Person  property 最简单的例子
2 Person1 用 property() 实现了相同的功能
3 Circle 动态属性，只有使用才计算

"""
import math


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

import pdb;pdb.set_trace()
a = Person('Guido')
print(a.first_name)  # Calls the getter
# a.first_name = 42  # Calls the setter
# del a.first_name  # Calls the deleter


class Person1:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)


print(Person1.name.fget)
print(Person1.name.fset)
print(Person1.name.fdel)


class Circle:
    """动态计算的property"""

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * self.radius ** 2


c = Circle(4.0)
print(c.radius)
print(c.area)  # Notice lack of ()