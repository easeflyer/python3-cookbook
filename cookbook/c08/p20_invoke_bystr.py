#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 通过字符串调用方法
Desc : 

知识点：
    1 通过 getattr 实现用字符串调用方法。
    2 通过 operator.methodcaller() 实现。
    3 注意二者语法上的不同。转变下语法可以相互替代。
"""

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # !r表示调用后面参数的__repr__()方法
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(2, 3)
d = getattr(p, 'distance')(0, 0)  # Calls p.distance(0, 0)

import operator

operator.methodcaller('distance', 0, 0)(p)

points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, 8),
    Point(3, 2)
]
# Sort by distance from origin (0, 0)
points.sort(key=operator.methodcaller('distance', 0, 0))
# points.sort(key=lambda p:getattr(p,'distance')(0,0)) # 替代方案
print(points)