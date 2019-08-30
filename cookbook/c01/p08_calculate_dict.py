#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 字典的数据运算
Desc : 
    如果你在一个字典上执行普通的数学运算，你会发现它们仅仅作用于键，而不是
值。或许你会尝试着使用字典的 values() 方法来解决这个问题。通常这个结果同样也不是你想要的。
因为缺少了 键信息，这个值是什么意义就缺少了。比如下例中 具体是那只股票。
为了更简单的完成这个操作，利用zip对字典的键值进行翻转。组成元组进行比较。不丢失任何信息。

知识点：
    1 zip(a,b) 把 a,b 打包成元组,元组数量，参考最短列表
    2 注意 python3 zip() 返回一个对象。zip 对象仅能访问一次。第二次访问数据为空。
    3 翻转字典的 键值，保存为元组。然后进行计算。利用 zip 的特性。
    4 利用 sorted 函数对 zip 对象进行排序。

sort 与 sorted 区别：
    sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
    list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法
    返回的是一个新的 list，而不是在原来的基础上进行的操作。

test2 演示了对 列表和 字典使用 min,max lambda 表达式中 x 参数的不同。
"""
def test1():
    a = [1,2,3]
    b = ['a','b','c','d']
    c = zip(a,b)    # c <zip object at 0x7f40890d3550>
    l1 = list(c)    # [(1, 'a'), (2, 'b'), (3, 'c')] c 会发生变化
    c1 = zip(*l1)    
    l2 = list(c1)   # [(1, 2, 3), ('a', 'b', 'c')]
    print(l1)
    print(l2)

def test2():
    d1 = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    l1 = [
        {'name':'ACME','price':45.23},
        {'name':'AAPL','price':612.78},
        {'name':'IBM','price':205.55},
        {'name':'HPQ','price':37.20},
        {'name':'FB','price':10.75}
    ]
    for item in d1: print(item) # ['ACME', 'AAPL', 'IBM', 'HPQ', 'FB']
    for item in l1: print(item) # 则 item 就是每个完整的对象。 
    min(d1,key = lambda x : d1[x])      # 'FB'
    min(l1,key = lambda x : x['price']) # {'name': 'FB', 'price': 10.75}





def calc_dict():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    min_price = min(zip(prices.values(), prices.keys()))
    # min_price is (10.75, 'FB')
    max_price = max(zip(prices.values(), prices.keys()))
    # max_price is (612.78, 'AAPL')

    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    print('prices_sorted:',prices_sorted)
    # prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
    #                   (45.23, 'ACME'), (205.55, 'IBM'),
    #                   (612.78, 'AAPL')]



    prices_and_names = zip(prices.values(), prices.keys())
    print(min(prices_and_names)) # OK
    print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

    min(prices) # Returns 'AAPL'
    max(prices) # Returns 'IBM'

    min(prices, key=lambda k: prices[k]) # Returns 'FB'
    max(prices, key=lambda k: prices[k]) # Returns 'AAPL'

    min_value = prices[min(prices, key=lambda k: prices[k])]

    prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
    min(zip(prices.values(), prices.keys()))
    # (45.23, 'AAA')
    max(zip(prices.values(), prices.keys()))
    # (45.23, 'ZZZ')

if __name__ == '__main__':
    #test1()
    calc_dict()