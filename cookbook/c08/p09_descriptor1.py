#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
描述符的基本概念


最容易理解的参考：
https://www.cnblogs.com/wongbingming/p/10781688.html
https://www.cnblogs.com/sfencs-hcy/p/10540469.html

这篇文章没看完跳过去了，环境不好，回头再看。
https://www.cnblogs.com/Jimmy1988/p/6808237.html

IBM 的。把这个看了：
https://www.ibm.com/developerworks/cn/opensource/os-pythondescriptors/index.html



属性查询优先级：（必须记住，这是前提）
    1 __getattribute__()， 无条件调用
    2 数据描述符：由 1 触发调用 （若人为的重载了该 __getattribute__() 方法，可能会调职无法调用描述符）
    3 实例对象的字典（若与描述符对象同名，会被覆盖哦）
    4 类的字典
    5 非数据描述符
    6 父类的字典
    7 __getattr__() 方法


'''
from pprint import pprint


class Tree(object):
    cattr = 'cattr1'
    def __init__(self,name):
        self.name = name
        self.cate = "plant"
    def __getattribute__(self,obj):
        ''' obj 调用的属性名 这里是 name '''
        print("哈哈")
        print("obj:",obj) # name
        re = object.__getattribute__(self,obj)
        print("re:",re)
        return re
    def func(self):
        print("func call")


def test3():
    # import pdb;pdb.set_trace()
    aa = Tree("大树")
    #print(aa.name)  # 读取 aa.name 的时候，首先输出了 哈哈
    #aa.func()
    print(aa.cattr)
'''
__getattribute__ 属性访问拦截器:
就是当这个类的属性被访问时，会自动调用类的__getattribute__方法。即在上面代码中，
当我调用实例对象aa的name属性时，不会直接打印，而是把 "name" 传进__getattribute__方法
（也就是参数obj），经过一系列操作后，再把name的值返回。就是最后的 return 的 re
Python中只要定义了继承object的类，就默认存在属性拦截器，只不过是拦截后没有进行任何操作，
而是直接返回。所以我们可以自己改写__getattribute__方法来实现相关功能，比如查看权限、
打印log日志等。

注意，拦截的属性，包括实例变量和方法，以及类属性。都会被拦截


'''










class Test(object):
    cls_val = 1
    def __init__(self):
        self.ins_val = 10

def test1():
    t = Test()
    pprint(Test.__dict__)
    pprint(t.__dict__)
    print( type(t) == Test )
    print('t.cls_val:',t.cls_val)
    t.cls_val = 20 # 只是给 t 实例增加了 cls_val 属性，并没有修改类属性
    pprint(t.__dict__)

'''
mappingproxy({'__dict__': <attribute '__dict__' of 'Test' objects>,
              '__doc__': None,
              '__init__': <function Test.__init__ at 0x7fbd4832b3b0>,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'Test' objects>,
              'cls_val': 1})  
{'ins_val': 10}
True
t.cls_val: 1

----------

可以看到 cls_val 属于类属性，而ins_val 是实例属性
但读取 t.cls_val 也可以读取到，这是python 内部搜索机制决定的，如果实例属性不存在
则尝试类属性->父类属性->__getattr__方法
'''




class Desc(object):  # 从 python > 3.6 比较高的版本后，默认继承自 object 
    
    def __init__(self,name):
        self.name = name
    def __get__(self, instance, owner):
        print("__get__...")
        print("self : \t\t", self)          # <__main__.Desc object 
        print("instance : \t", instance)    # <__main__.TestDesc object
        print("owner : \t", owner)          # <class '__main__.TestDesc'>
        print('='*30, "\n")
        
    def __set__(self, instance, value):
        print('__set__...')
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("value : \t", value)
        print('='*40, "\n")


class TestDesc(object):
    x = Desc('x1')
    y = 3
    def __init__(self):
        self.z = Desc('z1')
    def __getattribute__(self,attr):
        print("attr:",attr)
        re = object.__getattribute__(self,attr)
        print( "re:",re )   # 如果是 x 这里返回 None 但是上面确实也是执行了。
        return re


#以下为测试代码
def test2():
    t = TestDesc()
    t.x   # 如果 x 是描述符，实际上访问的就是 x.__get__(t,TestDesc)
    t.y
    t.z
'''
def __get__(self, instance, owner):
self        自身实例，容易理解记忆
instance    调用者，t.x t 就是 instance
owner       拥有者，注意是 TestDesc，这个类使用了 描述符

这里不用特别纠结他们三者的意义。 明确他们之间的关系即可。这是描述符定义的需要

上例：

访问 t.x 调用顺序：
    1 访问 __getattribute__。 其实就是从实例变量和类变量中搜索 x
    2 如果


'''









if __name__ == '__main__':
    # test1()
    test2()
    #test3() # __getattribute__ 案例