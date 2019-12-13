#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 弱引用
Desc : 

知识点：
    1 弱引用 就是个指针。不会增加引用计数。因此删除其他引用后，对象就会被立即回收。
    2 不会造成内存泄露问题。
"""

import weakref


class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


# Class just to illustrate when deletion occurs
class Data:
    def __del__(self):
        print('Data.__del__')


# Node class involving a cycle
class Node1:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        #child.parent = weakref.ref(self)    # 弱引用 直接被垃圾回收。
        child.parent = self                # 普通引用 必须强制回收。


def test1():
    a = Data()
    del a
    # print(a) NameError: name 'a' is not defined
    a = Node1()
    del a
    # print(a) 
    # UnboundLocalError: local variable 'a' referenced before assignment
    a = Node1()
    a.add_child(Node1())
    print('--------last del start------------')
    del a  # Not deleted (no message)
    print('--------force del start------------')
    import gc
    gc.collect()
    print('--------last del end------------')
    # print(a)
    print('11111111111111111')



test1()