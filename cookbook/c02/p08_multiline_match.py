#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 多行匹配
Desc : 

知识点：
    1 re.DOTALL 让 . 可以匹配任意字符。
    2 利用 小括号() 可以缩小保存匹配的范围。
"""
import re

# 小括号 缩小结果范围
def test1():
    text1 = "aaabbbccc111bbb222"
    reg1 = re.compile(r'c\d+b')  # ['c111b']
    reg2 = re.compile(r'c(\d+)b')  # ['111']
    print(reg1.findall(text1))
    print(reg2.findall(text1))


def multiline_match():
    comment = re.compile(r'/\*(.*?)\*/')
    text1 = '/* this is a comment */'
    text2 = '''/* this is a
    multiline comment */
    '''
    print(comment.findall(text1))
    print(comment.findall(text2))

    # 修正模式
    comment = re.compile(r'/\*((?:.|\n)*?)\*/')
    # comment = re.compile(r'/\*([\S|\s]*?)\*/') # 也可以
    print(comment.findall(text2))

    # 使用标志参数re.DOTALL，复杂匹配时不推荐
    comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
    print(comment.findall(text2))


if __name__ == '__main__':
    multiline_match()
    test1()