"""
注意相对导入方式 from . import grok 只用于 本文件也是一个包的情况。
也就是说用于 包和包之前的导入。目的是一个大包的迁移。
如果是一个顶层代码。或者普通的可执行脚本，就不要用相对导入。

！！通常有可执行的脚本，就不用相对导入

如果一定要执行，可以采用
`python -m p03.A.spam`   模块方式来执行。 返回正确结果。
`python p03/A/spam.py`  报错。不是一个模块


"""

from . import grok
# import grok

def func1():
    print("p03 A spam func1")

def func2():
    print("p03 A spam func2")

if __name__ == "__main__":
    grok.func1()