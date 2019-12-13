#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
    
10.5 包命名空间
    只要自己的包，目录和其他包目录结构一致。并且包里面没有 __init__.py 就可以和其他目录结构的包
合并成一个包。就好像文件放在相同目录一样。
    看一个包是不是命名空间，可以：包名.__file__   或者直接：包名。如果是命名空间显示 namespace
理解命名空间的概念，包里必须没有 __init__.py


10.9 将文件夹加入到 sys.path

有两种常用的方式将新目录添加到 sys.path

1. 第一种，你可以使用 PYTHONPATH 环境变量来添加。例如：

    bash % env PYTHONPATH=/some/dir:/other/dir python3
    Python 3.3.0 (default, Oct 4 2012, 10:17:33)
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import sys
    >>> sys.path
    ['', '/some/dir', '/other/dir', ...]
    >>>
    # 这样的环境变量可在程序启动时设置或通过 shell 脚本。

2. 第二种方法是创建一个.pth 文件，将目录列举出来，像这样：

    # myapplication.pth
    /some/dir
    /other/dir

这个.pth 文件需要放在某个 Python 的 site-packages 目录，通常位于/usr/local/
lib/python3.3/site-packages 或者 ~/.local/lib/python3.3/sitepackages。

3. 也可以通过代码导入：
import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), 'src')

"""

