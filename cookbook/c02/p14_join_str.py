#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 字符串合并
Desc : 

知识点：
    1 str.join(iter)   把可迭代对象组合成字符串。
    2 print(str1,str2,str3,sep='分隔符')
    3 不要用 + 加号连接大量字符。最好先收集起来然后用 join 效率更高。
    4 利用生成器表达式，转换数据为字符串。优化内存。

    5 combine 函数。分析如下：

分析：
    sample() 只负责生成，字符串片段，不管其他。
    combine() 负责从 sample() 读取片段并组合，如果读取的内容大于 maxsize 了
    则写入一次，继续读取，直到读取完毕。

    这就类似于“缓存”的功能，设置了最大的缓存，避免过大的内存占用。也避免了频繁的
    io操作。


"""


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


def join_str():
    parts = ['Is', 'Chicago', 'Not', 'Chicago?']
    print(' '.join(parts))
    print(','.join(parts))
    print(''.join(parts))

    # 使用+
    a = 'Is Chicago'
    b = 'Not Chicago?'
    c = 'ccc'
    print("plus:",a + ' ' + b)

    data = ['ACME', 50, 91.1]
    print(','.join(str(d) for d in data))


    print(a + ':' + b + ':' + c)    # Ugly
    print(':'.join([a, b, c]))      # Still ugly
    print(a, b, c, sep=':')         # Better

    # 混合方案
    # with open('filename', 'w') as f:
    #     for part in combine(sample(), 32768):
    #         f.write(part)
    print('----------------------combine-----------------')
    #print('='.join(sample()))
    for part in combine(sample(), 10):
        print(part)

if __name__ == '__main__':
    join_str()

'''
版本1 字符片段小时效率更高。减少了io曹邹。
版本2 字符片段大时效率更高，减少了临时的内存占用


# Version 1 (string concatenation) 
f.write(chunk1 + chunk2)

# Version 2 (separate I/O operations) 
f.write(chunk1)
f.write(chunk2)

'''