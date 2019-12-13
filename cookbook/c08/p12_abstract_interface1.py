#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 定义接口或抽象类
Desc : 
    非强制的方式定义“接口”和“抽象类”。
    我们看到 IStream() 有两个方法声明，但是并没有编写任何实质性的操作。这个特征非常
    符合“接口”的定义。
"""
class IStream():
    def read(self, maxbytes=-1):
        pass
    def write(self, data):
        pass


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        print('SocketStream.read')

    def write(self, data):
        print('SocketStream.write')



# class A(metaclass=ABCMeta):
#     @property
#     @abstractmethod
#     def name(self):
#         pass

#     @name.setter
#     @abstractmethod
#     def name(self, value):
#         pass

#     @classmethod
#     @abstractmethod
#     def method1(cls):
#         pass

#     @staticmethod
#     @abstractmethod
#     def method2():
#         pass

def test1():
    ss1 = SocketStream()
    ss1.read()
    ss1.write('data')
    print(f"ss1 isinstance SocketStream:{isinstance(ss1,SocketStream)}")
    print(f"ss1 isinstance IStream:{isinstance(ss1,IStream)}")


if __name__ == '__main__':
    test1()