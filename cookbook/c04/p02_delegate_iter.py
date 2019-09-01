#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 代理迭代
Desc : 

知识点：
    1 __iter__ 方法：对 Node 对象的迭代。被转移到 self._children 上。
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

def p_node(root):
    print(root)
    for node in root:
        p_node(node)

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)

    child3 = Node(3)
    child4 = Node(4)
    child5 = Node(5)
    child1.add_child(child3)
    child1.add_child(child4)
    child3.add_child(child5)


    # Outputs Node(1), Node(2)
    # for ch in root:
    #     print(ch)

    p_node(root)


    # 0
    #     1
    #         3
    #             5
    #         4
    #     2