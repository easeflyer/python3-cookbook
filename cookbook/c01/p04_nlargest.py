#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 返回集合中最大或最小的N个元素
Desc : 

关于 堆排序的基础知识：https://www.cnblogs.com/clnchanpin/p/7217950.html
"""
import heapq


def test1():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
    print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]    

def main():
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
    print(cheap)
    print(expensive)

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heapq.heapify(nums)
    print(nums)
    print(heapq.heappop(nums))
    print(heapq.heappop(nums))
    print(heapq.heappop(nums))


if __name__ == '__main__':
    test1()
    #main()

