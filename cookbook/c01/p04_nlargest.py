#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 返回集合中最大或最小的N个元素
Desc : 

关于 堆排序的基础知识：https://www.cnblogs.com/clnchanpin/p/7217950.html
参考练习：https://www.jianshu.com/p/801318c77ab5
创建堆

方法一：heapq.heappush 把数值逐一加入堆 heapq1()

方法二：heap.heapify(list) 转换列表为 堆结构。

"""
import heapq




def heapq1():
    """
    题目：heapq.heappush 把数值逐一加入堆
    用 _ 表示无用的数据变量
    heap 为空堆数组。利用  heapq.heappush 加入数据。注意加入后的数据规则。
    heap[0] 永远都是最小值
    """
    nums = [2, 3, 5, 1, 54, 23, 132]
    heap = []
    for num in nums:
        heapq.heappush(heap, num)  # 加入堆

    print(heap[0])  # 如果只是想获取最小值而不是弹出，使用heap[0]
    print(heap)
    print([heapq.heappop(heap) for _ in range(len(nums))])  # 堆排序结果

def heapq2():
    """
    通过 heapq.heapify(nums) 把列表直接
    """
    nums = [2, 3, 5, 1, 54, 23, 132]
    heapq.heapify(nums)
    print("heap_list:",nums)
    print("sort_list:",[heapq.heappop(nums) for _ in range(len(nums))])  # 堆排序结果    



def test1():
    """
    利用 heapq 模块，从列表中取出 最大3个数，最小3个数
    """
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
    print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]    

def main():
    """
    知识点：
        1 nsmallest(n,list,key) 从列表list中取出n个最小的元素
        2 nlargest(n,list,key)  从列表list中取出n个最大的元素
        3 key 参数：如果list 元素是dict，则以 key为比较的字典元素，这里是比较 price
    """
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print("cheap:",cheap)
    print("expensive:",expensive)

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heapq.heapify(nums)
    print(nums)
    print(heapq.heappop(nums))
    print(heapq.heappop(nums))
    print(heapq.heappop(nums))


if __name__ == '__main__':
    #heapq1()
    #heapq2()
    #test1()
    main()

