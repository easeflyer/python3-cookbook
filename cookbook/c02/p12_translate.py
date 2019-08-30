#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: str的 translate 方法清理文本
Desc : 对于特殊字符的清理。本案例给出了一些解决方案。

translate(table[,deletechars]) 
    方法根据参数table给出的表(包含 256 个字符)转换字符串的字符,要过滤掉的字符放到 
    deletechars 参数中。




"""
import unicodedata
import sys


def clean_spaces(s):
    """普通替换使用replace最快"""
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s


def translate_str():
    s = 'pýtĥöñ\fis\tawesome\r\n'
    print(s)

    remap = {
        ord('\t'): ' ',
        ord('\f'): ' ',
        ord('\r'): None  # Deleted
    }

    a = s.translate(remap)
    print("a:",a)

    # 删除和音符
    cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                             if unicodedata.combining(chr(c)))
    b = unicodedata.normalize('NFD', a)
    print(b)
    print(b.translate(cmb_chrs))

    # unicode数字字符映射到ascii字符
    digitmap = {c: ord('0') + unicodedata.digit(chr(c))
                for c in range(sys.maxunicode)
                if unicodedata.category(chr(c)) == 'Nd'}
    print(len(digitmap))
    x = '\u0661\u0662\u0663'
    print(x.translate(digitmap))

    # 先标准化，然后使用encode和decode函数
    b = unicodedata.normalize('NFD', a)
    print(type(b))
    print(b.encode('ascii', 'ignore').decode('ascii'))



def test1():
    '''
    上例中，手动创建的 remap。  本例中使用 str.maketrans 创建更加方便。
    '''
    s = 'pýtĥöñ\fis\tawesome\r\n'
    inStr = '\t\f\r'
    outStr = '   '
    remap = str.maketrans(inStr,outStr)
    print('---------------------------------test1()----------------')
    print(s.translate(remap))

if __name__ == '__main__':
    translate_str()
    test1()
