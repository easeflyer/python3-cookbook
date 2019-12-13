#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 控制导入内容
Desc : 
"""

# somemodule.py
def spam():
    print('spam exec.....')


def grok():
    print('grok exec.....')

def foo():
    print('foo exec.....')

blah = 42
# Only export 'spam' and 'grok'
__all__ = ['spam', 'grok']


"""
p03 使用相对路径 导入包内的 子模块

from . import grok  导入当前路径下的 grok 子模块
from ..B import bar 导入上级路径 B 包内的子模块 bar

注意：
    1 也可以用“包绝对路径”，缺点是你想重新组织包，受到一定制约。
    2 . .. 语法只支持“包” 非包的文件夹关系 并不支持。

"""