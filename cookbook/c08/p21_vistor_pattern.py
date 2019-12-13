#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 观察者模式
Desc : 

代码分析：
    1 Node, Add, Sub, Mul.. 定义了若干类，代表“运算的名称”。并没有具体实现。
    2 只有 Number 类包含了存储具体数值的功能。
    3 NodeVisitor 基类，visit 提供了根据 node的类型名称（也就是classname）调用对应的方法的功能。
        visit 是核心，他提供了根据具体类型访问具体方法的功能。
    4 Evaluator 求值类实现了 NodeVisitor 具备了以上能力，并实现了若干针对不同 Node 的运算方法。
        其中使用了递归，如果 type(node) 是Number 则会结束递归。否则继续执行 visit 处理左右
    5 test1: 首先定义了 t1-t4 四个相关的元算。然后对 t4 进行求值。

"""


class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


class NodeVisitor:
    def visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_Negate(self, node):
        return -node.operand


def test1():
    '''
    Evaluator [i'væljueitə] n. 求值程序
    '''
    # Representation of 1 + 2 * (3 - 4) / 5
    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(2), t1)
    t3 = Div(t2, Number(5))
    t4 = Add(Number(1), t3)
    print(t4)
    e = Evaluator()
    print(e.visit(t4))

    s = StackCode()
    print(s.generate_code(t4))



# 这个例子看的不太明白。
class StackCode(NodeVisitor):
    def generate_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions

    def visit_Number(self, node):
        self.instructions.append(('PUSH', node.value))

    def binop(self, node, instruction):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append((instruction,))

    def visit_Add(self, node):
        self.binop(node, 'ADD')

    def visit_Sub(self, node):
        self.binop(node, 'SUB')

    def visit_Mul(self, node):
        self.binop(node, 'MUL')

    def visit_Div(self, node):
        self.binop(node, 'DIV')

    def unaryop(self, node, instruction):
        self.visit(node.operand)
        self.instructions.append((instruction,))

    def visit_Negate(self, node):
        self.unaryop(node, 'NEG')


class HTTPHandler:
    def handle(self, request):
        methname = 'do_' + request.request_method
        getattr(self, methname)(request)
    def do_GET(self, request):
        pass
    def do_POST(self, request):
        pass
    def do_HEAD(self, request):
        pass


if __name__ == "__main__":
    test1()