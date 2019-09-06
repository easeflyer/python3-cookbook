#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 

知识点：

    2 hasattr(), getattr(), setattr()
        hasattr(obj,'name') 查看 对象是否包含某个属性。
        getattr(obj.'name') 读取和执行对象的某个属性。
        setattr(obj,'name',value) 可以设置属性值

        __getattr__(self,name) 如果调用类没有的属性，就会触发这个方法，字符串作为name 

    3 理解 supper 的用途和原理。理解 __mro__的用途。见 test2()
"""


class A:
    def __init__(self):
        self.x = 123
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        super().spam()  # Call parent spam()
        print(self.x)

class A1:
    def __init__(self):
        self.y = 2


class B1(A1):
    def __init__(self):
        super().__init__()  # 如果这里不执行，则 A1.__init__ 不会被执行。因为覆盖了。
        self.y += 1
    def spam(self):
        print("B1 y:",self.y)


class Proxy():
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)  # Call original __setattr__
        else:
            setattr(self._obj, name, value)

class P1(Proxy):
    pass        


class Base:
    def __init__(self):
        print('Base.__init__')


class AA(Base):
    def __init__(self):
        super().__init__()
        print('AA.__init__')


class BB(Base):
    def __init__(self):
        super().__init__()
        print('BB.__init__')


class CC(AA, BB):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('CC.__init__')


def test1():
    CC()
    print(CC.__mro__)    


class A3:
    def spam(self):
        print('A3.spam')
        super().spam()


class B3:
    def spam(self):
        print('B3.spam')


class C3(A3, B3):
    pass

def test2():
    print(C3.__mro__)
    C3().spam()

# 测试 __init__ 的执行。
# hasattr() getattr() setattr()
def test3():
    b = B()
    b.spam()
    b1 = B1()
    b1.spam()

    print('hasattr(b, \'spam\'):',hasattr(b, 'spam'))
    print('hasattr(b, \'y\'):',hasattr(b, 'y'))
    setattr(b,'y',3)
    print('hasattr(b, \'y\'):',hasattr(b, 'y'))
    print('getattr(b,\'y\'):',getattr(b,'y'))
    getattr(b,'spam')()
    
    print('------------------proxy--------------------')
    import pdb;pdb.set_trace()
    o1 = A()
    p1 = P1(o1)
    setattr(p1,'p1','p11')
    setattr(p1,'_p2','p22')
    print(p1.p1)
    print(p1._p2)
    print('333')
    print('333')



if __name__=="__main__":
    # test1()
    test2()
    # test3()