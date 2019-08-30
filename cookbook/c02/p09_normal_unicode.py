#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: unicode字符串标准化表示
Desc : 

知识点：
    1 normalize 函数 对字符串进行标准化。把两种不同表示的uncode 标准化为一种。
    2 当处理用户输入的时候，进行标准化处理就比较重要了，影响到后期存储和检索。
"""
import unicodedata


def nor_unicode():
    s1 = 'Spicy Jalape\u00f1o'
    s2 = 'Spicy Jalapen\u0303o'
    print(s1, s2)
    print(s1 == s2)
    print(len(s1), len(s2))

    # 先将文本标准化表示
    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)
    print(t1 == t2)
    print(ascii(t1))

    t3 = unicodedata.normalize('NFD', s1)
    t4 = unicodedata.normalize('NFD', s2)
    print(t3 == t4)
    print(ascii(t3))

    # 扩展的NFKC和NFKD
    s = '\ufb01'  # A single character
    # s = 'n\u0303'  # n\u0303 是一个独特的字符 m\u0303 则不成立。
    print("0:",s, len(s))
    print("1:",unicodedata.normalize('NFC', s), len(unicodedata.normalize('NFC', s)))
    print("2:",unicodedata.normalize('NFD', s), len(unicodedata.normalize('NFD', s)))
    print("3:",unicodedata.normalize('NFKC', s), len(unicodedata.normalize('NFKC', s)))
    print("4:",unicodedata.normalize('NFKD', s), len(unicodedata.normalize('NFKD', s)))

    # 消除变音符 把 n 上面的波浪线去掉了。
    t1 = unicodedata.normalize('NFD', s1)
    print(''.join(c for c in t1 if not unicodedata.combining(c)))


if __name__ == '__main__':
    nor_unicode()

