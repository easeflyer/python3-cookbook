#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 定义接口或抽象类
Desc : 
    python 对于“抽象类” 和 “接口”的实现方案。通常如果没有特殊需求，我们也可以比较
简单的定义一个空类，为抽象类或者接口。并不进行强制性的而约束和定义。而只是我们的业务
隐含的约定。参考(p12_abstract_interface1.py)

知识点：
    1 ABCMeta 定义抽象类, metaclass （元类） 用于定义类。
    2 抽象类不可以直接实例化。
    3 @abstractmethod 还能注解静态方法、类方法和 properties 
    4 不建议做强制的限制，Python 的理念更倾向于灵活。程序员做更好的隐含约定更好。
        强制限制，会让程序看起来更加复杂。

"""
from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass


def test1():
    # is1 = IStream()  # 无法直接实例化 抽象类
    import io
    IStream.register(io.IOBase)
    f = open('./p12_abstract_interface.py')
    print("f is IStream:",isinstance(f,IStream))


if __name__ == "__main__":
    test1()