
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 最短匹配，非贪婪模式匹配
Desc : 

知识点：
    1 贪婪模式，非贪婪模式 ? 号可以让算法，找到最短的匹配。
"""
import re


def short_match():
    # 贪婪模式
    str_pat = re.compile(r'\"(.*)\"')
    text1 = 'Computer says "no."'
    print(str_pat.findall(text1))
    text2 = 'Computer says "no." Phone says "yes."'
    print(str_pat.findall(text2))

    # 非贪婪模式
    str_pat = re.compile(r'\"(.*?)\"')
    print(str_pat.findall(text2))

if __name__ == '__main__':
    short_match()

