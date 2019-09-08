#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 字符串令牌化
Desc : 

知识点：
    1 scanner 的使用。

scanner:
    a = scanner.match() 每次调用返回一个匹配对象。
    (?P<TOKENNAME>) 是给分组命名
    a.lastgroup     是匹配分组的名称。也就是给小括号括起来的正则命名。
    a.group()       返回分组匹配的结果字串。
    
注意令牌化，需要对令牌正则 全覆盖，如果有任何一个字符无法匹配将会导致问题。比如 WS = ""


namedtuple
    在 generate_tokens 生成器函数中。还用到了 namedtuple 命名元组。


"""
import re
from collections import namedtuple


def tokenize_str():
    text = 'foo = 23 + 42 * 10'
    tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
              ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
    NUM = r'(?P<NUM>\d+)'       # 数字
    PLUS = r'(?P<PLUS>\+)'      # 加号
    TIMES = r'(?P<TIMES>\*)'    # 乘号
    EQ = r'(?P<EQ>=)'           # 等号
    WS = r'(?P<WS>\s+)'         # 空格

    master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

    scanner = master_pat.scanner('foo = 42')
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)
    print((a.lastgroup, a.group()))
    a = scanner.match()
    print(a)

    # 实际生成器代码

    # Example use
    for tok in generate_tokens(master_pat, 'foo = 42'):
        print(tok)
    # Produces output
    # Token(type='NAME', value='foo')
    # Token(type='WS', value=' ')
    # Token(type='EQ', value='=')
    # Token(type='WS', value=' ')
    # Token(type='NUM', value='42')

    print('{:>60s}'.format('text'))  # 右对齐的 高级分隔符
    tokens = (tok for tok in generate_tokens(master_pat, text)
              if tok.type != 'WS')
    for tok in tokens:
        print(tok)

    print('*'*40)

    LT = r'(?P<LT><)'
    LE = r'(?P<LE><=)'
    EQ = r'(?P<EQ>=)'
    master_pat = re.compile('|'.join([LE, LT, EQ])) # Correct
    # master_pat = re.compile('|'.join([LT, LE, EQ])) # Incorrect
    # 注意 LE <= 要写在前面，优先匹配，如果写在后面，那么将会被分开匹配。



def generate_tokens(pat, text):
    ''' 返回命名元组'''
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


if __name__ == '__main__':
    tokenize_str()
