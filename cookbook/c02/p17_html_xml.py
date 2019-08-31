#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 处理html和xml文本
Desc : 

知识点：
    1 html.escape() 用实体替换字符, html.unescape() 相反
    2 errors='xmlcharrefreplace' 替换不符合编码要求的字符。
    3 注意部分 已经不支持的函数。

encode 把 s 编码为 ascii ，但字符串中包含无法编码的字符，会造成错误。使用
errors='xmlcharrefreplace' 即可对不符合要求的字符进行替换。

"""
import html


def html_xml():
    s = 'Elements are written as "<tag>text</tag>".'
    print(s)
    print(html.escape(s))

    # Disable escaping of quotes 不替换引号
    print(html.escape(s, quote=False))

    s = 'Spicy Jalapeño'
    # print(s.encode('ascii'))  # 报错
    print(s.encode('ascii', errors='xmlcharrefreplace'))


def html_parser():
    from html.parser import HTMLParser
    from xml.sax.saxutils import unescape
    s = 'Spicy &quot;Jalape&#241;o&quot.'
    p = HTMLParser()
    # print(p.unescape(s)) 已经从 python 3.5 被移除。
    print(html.unescape(s))
    t = 'The prompt is &gt;&gt;&gt;'
    print(html.unescape(t))
    print(unescape(t))

if __name__ == '__main__':
    html_xml()
    print('------------html_parser------------------')
    html_parser();
