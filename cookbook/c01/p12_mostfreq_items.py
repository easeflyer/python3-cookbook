#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 查找出现次数最多的元素
Desc : 

知识点：
    1 Counter 统计列表中 元素出现的次数。返回元组列表。
    2 Counter.most_common(3) 返回最高频的3个。
    3 Counter.update(morelist) 更新计数
    4 Counter 对象直接进行数学运算

Counter 的数学运算的用途？
    加减：对相同词 的 计数进行了加减。
    | 或运算： 把两个集合去重合并，并没有相加，
    & 与运算：取两个集合相同，也没有进行加减运算

"""
from collections import Counter

def most_freqency():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    word_counts = Counter(words)
    print('Counter(words):',word_counts)
    print('word_counts[look]:',word_counts["look"])
    word_counts["look"] += 1 # 手动调整数值
    print('word_counts[look]:',word_counts["look"])
    print(type(word_counts))  # <class 'collections.Counter'>
    # 出现频率最高的3个单词
    top_three = word_counts.most_common(3)
    print(top_three)

    word_counts.update(['my','my','my','info'])
    top_three = word_counts.most_common(3)
    print(top_three)
    # Outputs [('eyes', 8), ('the', 5), ('look', 4)]

def counter_calculate():  #  ['kælkjulet]
    a = ['aaa','bbb','ccc','ddd','aaa','bbb','aaa']
    b = ['ccc','ddd','eee']
    count1 = Counter(a)
    count2 = Counter(b)
    count3 = count1 + count2
    count4 = count1 - count2  # | & 运算 也可以
    print(f"{count1}\n{count2}\n{count3}\n{count4}\n{count5}")

if __name__ == '__main__':
    #most_freqency()
    counter_calculate()

