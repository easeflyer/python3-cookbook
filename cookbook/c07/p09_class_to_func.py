#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 单方法类转换为函数
Desc : 大多数情况下，可以使用 闭包 来将单个方法的类转换成函数。
    大部分情况下，你拥有一个单方法类的原因是需要存储某些额外的状态来给方法
    使用。比如，定义 UrlTemplate 类的唯一目的就是先在某个地方存储模板值，以便将来
    可以在 open() 方法中使用。
    使用一个内部函数或者闭包的方案通常会更优雅一些。简单来讲，一个闭包就是
    一个函数，只不过在函数内部带上了一个额外的变量环境。闭包关键特点就是它会记
    住自己被定义时的环境。因此，在我们的解决方案中， opener() 函数记住了 template
    参数的值，并在接下来的调用中使用它。
    任何时候只要你碰到需要给某个函数增加额外的状态信息的问题，都可以考虑使
    用闭包。相比将你的函数转换成一个类而言，闭包通常是一种更加简洁和优雅的方案

知识点：
    1 如何用函数替代类。
    2 闭包。以上说明 也很好的介绍了闭包的概念。

"""

from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))

# Example use. Download stock data from yahoo
yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))


# =======================闭包方案=================
def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

# Example use
yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))
