#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 函数默认参数
Desc : 

知识点：
    1 函数参数的默认值，应该是“不可变对象” 比如：简单数据类型，或者元组

如果给默认值赋值了一个对象，也就是“引用” 或者叫“指针”。就意味着，这个函数对象的默认值
会发生变化。如果这个默认值对象发生变化了，那么这个参数因为是引用的这个值，因此也发生了
变化。 造成函数调用的结果不一致。  见 test1()

    2 is 操作符对对象进行判断。
    3 判断用户是否 传递了 第二个参数：

自定义一个变量，这里的思路是用户不可能去传递这个 _no_value 实例作为输入    
"""

def spam(a, b=42):
    print(a, b)

spam(1) # Ok. a=1, b=42
spam(1, 2) # Ok. a=1, b=2

_no_value = object()

def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')



def test1(x,y=[2,2,2]):
    print('y:',y)
    return y

def test2(x,y=None):
    # if not y: print("if Not Y")   不建议这么写
    print("y is None") if y is None else print(y)

if __name__== '__main__':
    y1 = test1(3)
    y1[1] = 3       # 对 y1 的修改，影响到了test1 函数的默认值
    y2 = test1(4)

    test2(2,3)
    test2(2)