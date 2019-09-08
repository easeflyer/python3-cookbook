#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 无穷大与NaN
Desc : 

知识点：
    1 NaN值的一个特别的地方时它们之间的比较操作总是返回False，因此只能用 math.isnan()测试
    2 NaN值会在所有操作中传播，而不会产生异常。
    3 

"""
import math

def inf_nan():
    a = float('inf')    # 正无穷大
    b = float('-inf')   # 负无穷大
    c = float('nan')    # nan
    
    print('math.isinfo:',math.isinf(a))
    print('math.isnan:',math.isnan(c))
    print(a + 45)
    print(a + 45 == a)
    print(a * 10 == a)
    print(10 / a)

    # undifined
    print('a/a:',a / a)
    print('a+b:',a + b)

    print(c + 23)
    print(c / 2 == c)  # False ?


if __name__ == '__main__':
    inf_nan()

