#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 正则式分割字符串
Desc : 

知识点：
    1 re.split(r'正则分隔符', line) 用正则分割字符串，返回列表。
    2 正则分隔符中如果出现() 则“捕获分组” 也会出现在列表中。;,和空格
    3 “非捕获分组” (?:...) 不会保存到列表中。

切片注解：[start:end:step]
    
    fields          ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
    fields[::2]     ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
    fields[1::2]    [' ', ';', ',', ',', ',']
    为了使用 zip 组合，需要对 fields[1::2] + [''] 变为6个元素。
    最后通过 列表生成式合并 v+d, 通过 join 链接成字符串。
"""
import re


def split_str():
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    print(re.split(r'[;,\s]\s*', line))
    print(re.split(r'(;|,|\s)\s*', line))
    fields = re.split(r'(;|,|\s)\s*', line)
    values = fields[::2]
    delimiters = fields[1::2] + ['']
    print(''.join(v+d for v,d in zip(values, delimiters)))

if __name__ == '__main__':
    split_str()

