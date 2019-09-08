#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 利用numpy执行数组运算
Desc : 涉及到数组的重量级运算操作，可以使用 NumPy 库。 NumPy 的一个主要特征是它会给Python

提供一个数组对象，相比标准的Python列表而已更适合用来做数学运算

知识点：
    1 普通数组 * 2, 横向扩展为 2个数组
    2 普通数组 相加，简单横向扩展为两个数字叠加。
    3 numpy 数组 *2 是矩阵乘法，每个元素都乘2 ， numpy 操作作用于每个元素。
    4 numpy 数组相加，是矩阵相加，每个元素相加。

    5 numpy 还提供了大量通用函数。这些函数可以替代 math 包中的类似函数。 numpy 的这些通用函数
      可以直接作用与每个数组元素，计算迅速。比采用 math 函数，循环计算，快得多。
    6 numpy 很容易构造一个超大的数组，并且以上计算仍然是作用于每个元素。

    7 numpy.array 二维数组，选取一行，选取一列。
    8 print(np.where(a < 10, a, 10)) 矩阵中所有 <10 的元素， 不符合的元素用 10 填充


numpy.array 选取一列的语法 arr[第一维，第二维] arr[:,1] 意思就是 第一维度全选，第二维度第二下标。

"""
import numpy as np


def array_numpy():
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]
    print(x * 2)
    print(x + y)

    # Numpy arrays
    ax = np.array([1, 2, 3, 4])
    ay = np.array([5, 6, 7, 8])
    print(ax * 2)
    print(ax + ay)
    print(ax * ay)

    print(f(ax))
    print(np.sqrt(ax))
    print(np.cos(ax))

    # 大数组
    # np.zeros 构造一个矩阵，shape 横纵维度， dtype 数据精度。
    grid = np.zeros(shape=(10000, 10000), dtype=float)
    grid += 10
    print(grid)
    print(np.sin(grid))

    # 二维数组的索引操作
    print('------------------------------------二维数组操作 -------------')
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(a)
    print(a[1])     # Select row 1
    print(a[:, 1])  # Select column 1
    # Select a subregion and change it
    # 选择一个区域，然后改变这个区域的数值。注意数组是按照引用计算的。直接改变原数组。
    print(a[1:3, 1:3])
    a[1:3, 1:3] += 10
    print(a)

    # Broadcast a row vector across an operation on all rows
    print(a + [100, 101, 102, 103])
    # Conditional assignment on an array
    print(np.where(a < 10, a, 10))



def f(x):
    return 3 * x ** 2 - 2 * x + 7


if __name__ == '__main__':
    array_numpy()