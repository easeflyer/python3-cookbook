#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 自定义迭代器协议
Desc : 

1 目前为止，在一个对象上实现迭代最简单的方式是使用一个生成器函数


DepthFirstIterator 比较繁琐，略过。（除非必要不用这个方式）
直接用上节介绍的，生成器实现自定义即可。



"""


class Node:
    '''
    Node 每个节点包含：1 自身的值 _value 2 孩子节点
    '''
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self): # __repr__ 针对程序员的输出 __str__ 针对用户的输出
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self      # 先返回自己
        for c in self:  # 随后返回自己的子节点
            yield from c.depth_first()


class Node2:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    '''
    Depth-first traversal
    '''

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        # If processing a child, return its next item
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        # Advance to the next child and start its iteration
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
        # Outputs Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)

# 0
# 1   2
# 34  5

