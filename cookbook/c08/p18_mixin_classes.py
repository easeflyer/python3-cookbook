#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 混入类
Desc : 如果单独使用Minxin类没有任何意义，但是当利用多继承和其他类配合后就有神奇效果了。
    Mixin也是多继承的主要用途。

知识点：
    1 __getitem__, __setitem__, __delitem__
     是对序列的操作。添加了这几个魔术方法，影响到实例的 a['name'] 的读取赋值和删除
    



"""


class LoggedMappingMixin:
    """
    Add logging to get/set/delete operations for debugging.
    """
    __slots__ = ()  # 混入类都没有实例变量，因为直接实例化混入类没有任何意义

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)


class SetOnceMappingMixin:
    '''
    Only allow a key to be set once.
    如果key 存在就报错。因此只能设置一次
    '''
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class StringKeysMappingMixin:
    '''
    Restrict keys to strings only
    '''
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')
        return super().__setitem__(key, value)


class LoggedDict(LoggedMappingMixin, dict):
    pass

def test1():
    '''
    从上面的定义可以看到，LoggedDict 类继承了LoggedMappingMixin 和 dict
    本质上 LoggedDict 是一个 dict，他们属于继承关系。
    而LoggedMappingMixin 则是提供了特定的功能。概念上并没有父子关系。cookbook中所述：
    你有很多有用的方法，想使用它们来扩展其他类的功能。但是这些类并没有任何继承的关系。
    因此你不能简单的将这些方法放入一个基类，然后被其他类继承。
    本例中 LoggedDict  为字典模拟添加了 Log 功能。
    '''
    d = LoggedDict()
    d['x'] = 23     # setitem
    print(d['x'])   # getitem      
    del d['x']      # delitem

from collections import defaultdict


class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass

def test2():
    '''
    defaultdict 具有默认值的 dict
    '''
    d = SetOnceDefaultDict(list)
    d['x'].append(2)
    d['x'].append(3)
    # d['x'] = 23  # KeyError: 'x already set'


def LoggedMapping(cls):
    """第二种方式：使用类装饰器
    这个类装饰器非常值得学习。充分体现了 类装饰器只是 函数的语法糖
    @classdecorator
    class cls1
    也就是 cls1 = classdecorator(cls1)
    
    """
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return cls_getitem(self, key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return cls_delitem(self, key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls


@LoggedMapping
class LoggedDict1(dict):
    pass

def test3():
    ld1 = LoggedDict1()
    ld1['id'] = 33
    ld1['name'] = "zhangsan"
    print(ld1['name'])
    del ld1['name']



if __name__ == "__main__":
    test1()
    test2()
    test3()