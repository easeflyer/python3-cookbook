#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 通过元类控制实例的创建
Desc : 

知识点：
    1 元类就是用来定义类的。他的实例就是“类对象”
    2 元类内部的 self 实际上就是 类对象。self() 才是实例对象。
    3 元类定义要继承 type
    4 利用元类来实现 这几个功能，代码更加优雅。虽然多了一个元类（高级功能）但可读性更好更直观，
    5 元类参考印象笔记 oop高级部分
    6 元类的 __new__ def __new__(cls, clsname, bases, clsdict):


class NoInstances(type):
    这是一个元类的定义。他的实例是一个类对象。那么类对象的实例化()，调用的就是
    元类的__call__。 __call__ 的作用就是：让实例可以callable ，元类的实例就是类
    因此类的实例化就是 call 这个对象。

class Spam(metaclass=NoInstances):
    Spam 使用元类来定义。
    因此如果执行 Spam 会被元类的 __call__ 代理。会报错。
    因此 Spam 只能调用静态方法，不能被实例化。

class Singleton(type):
    实现单例模式的元类
    __call__ 使用本元类定义的类，实例化时会被__call__ 代理。
    元类的实例，建立了属性：__instance 用于保存被定义的类的实例。当__call__执行时
    首先判断__instance 是否已经存在，如果存在直接返回。不存在则调用原有的__call__返回实例。


元类的 __new__ 
因为元类的 __new__ 不是我们自己编写的 python 代码调用。
def __new__(cls, clsname, bases, clsdict):
    1 当前准备创建的类的对象（类对象，上例中就是 MyList 所指向的对象）；
        注意：元类是用来创建类的，这里 cls 就是被创建类的类对象。而不是元类自身。
        但如果不是元类，则代表的是类自身。
    2 类的名字；
    3 类继承的父类集合；
    4 类的方法集合。


元类相比普通类的特殊之处有那些？
    1 元类继承type
    2 元类的实例是“类对象”，类对象的实例就是普通类实例化的结果。




遗留问题：
    1 __call__ 和 __new__ 的关系和顺序。
    2 self.__instance = super().__call__(*args, **kwargs) 如何完成的实例化？
        被定义的类的 __init__ 什么时候执行？
"""


# 元类，目的是：阻止子类实例化。
# __call__ 让此类的实例为：callable, 也就是执行本方法。
class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


# Example
# Spam 用 metaclass NoInstances 定义，因此无法实例化。
# grok 方法只能定义为 staticmethod 通过类的方式调用。
class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok',x)

def test1():
    #s1 = Spam() # 报错 TypeError: Can't instantiate directly
    Spam.grok(3)
test1()


# 元类定义
# 元类定义的 self.__instance 用于保存 实例的引用。
# 元类的实例 就是 类对象。因此 __call__ 就是子类的实例化过程。
# __call__ 当子类实例化的时候。判断是否已经保存了实例。如果有则取出
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs) # 固定用法 记住即可。

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


# Example
class Spam1(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')

def test2():
    s2 = Spam1()
    s3 = Spam1()
    s4 = Spam1()
    print(f"s2 is s3:{s2 is s3} s3 is s4:{s3 is s4}")
test2()




# weakref 弱引用。不增加引用计数，不影响垃圾回收。不影响原有对象间应用关系。
# 因此使用 weakref 非常适合用在 缓存中。缓存不应该影响原有程序逻辑。
import weakref

# 定义元类
# __call__ 子类实例化的时候调用。
class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


# Example
class Spam2(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name




