#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 隐藏私有属性
Desc : 

知识点：
    1 python 并不限制 私有属性。仅以命名进行约定。
    2 单下划线 代表私有属性的约定 适用于类以及模块，模块级别的函数。
    3 双下划线命名的属性/方法，无法被继承覆盖重写。

关于双下划线：
    类 C 继承了 类B 之后。c 的实例 c1的所有成员包括：
    _B__private_method()  注意名称
    _C__private_method()  名称前缀
    _private_b()
    _private_c()
    从 c1 的成员可以看到 __private_method 并没有被覆盖，而是以不同的前缀都保留下来
    的。因此可以看到python的这个特性，组织了子类覆盖父类的某些属性。


"""


class A:
    def __init__(self):
        self._internal = 0  # An internal attribute
        self.public = 1  # A public attribute

    def public_method(self):
        '''
        A public method
        '''
        pass

    def _internal_method(self):
        pass


class B:
    def __init__(self):
        self.__private = 0

    def _private_b(self):
        pass
    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1  # Does not override B.__private
    def _private_c(self):
        pass
    # Does not override B.__private_method()
    def __private_method(self):
        pass
    

if __name__ == '__main__':
    import pdb;pdb.set_trace()
    c1 = C()