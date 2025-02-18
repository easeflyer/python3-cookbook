
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 字节字符串操作
Desc : 

知识点：
    1 针对字节字符串的 搜索操作，也要用字节字符串。否则会报错。
    2 字节字符串下标取值，返回的是整数，而不是字符。
    3 想格式化字节字符串，你得先使用标准的文本字符串，然后将其编码为字节字符串
"""
import re


def byte_str():
    data = b'Hello World'
    print(data[0:5])
    print(data.startswith(b'Hello'))
    print(data.split())
    print(data.replace(b'Hello', b'Hello Cruel'))

    # 字节数组
    data = bytearray(b'Hello World')
    print(data[0:5])
    print(data.startswith(b'Hello'))
    print(data.split())
    print(data.replace(b'Hello', b'Hello Cruel'))

    # 正则式
    data = b'FOO:BAR,SPAM'
    print("re.split:",re.split(b'[:,]',data))

    # 字节字符串打印不美观
    s = b'Hello World'
    print(s)
    print(s.decode('utf-8'))

    print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))


if __name__ == '__main__':
    byte_str()