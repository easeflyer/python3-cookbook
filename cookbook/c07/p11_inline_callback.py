#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 内联回调函数
Desc : 

注意本案例的执行流程比较复杂。
需要认真一步一步的仔细确认。 要对 yield 和 装饰器有准确的理解。
"""
from queue import Queue
from functools import wraps


def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


class Async:
    '''仅仅记录了 函数 和 参数，其他什么都没干'''
    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    ''' 装饰器
    被装饰函数 func
    func执行结果 f, 从 f.send 可知 f 是一个协程。
    f 协程 yeild 返回给 a
    '''
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            print('1' * 15)
            result = result_queue.get()
            print('2' * 15)
            try:
                print('3' * 15)
                print('result={}'.format(result))
                a = f.send(result)
                print('4' * 15)
                apply_async(a.func, a.args, callback=result_queue.put)
                print('5' * 15)
            except StopIteration:
                break

    return wrapper


def add(x, y):
    return x + y


@inlined_async
def test():
    print('start'.center(20, '='))
    r = yield Async(add, (2, 3))
    print('last={}'.format(r))
    r = yield Async(add, ('hello', 'world'))
    print('last={}'.format(r))
    # for n in range(10):
    # r = yield Async(add, (n, n))
    # print(r)
    # print('Goodbye')
    print('end'.center(20, '='))


# ----附加案例--------------------------------------------------------
def dfunc(func):
    @wraps(func)
    def wrapper(*args):
        f = func()
        print(1)
        print(1)
    return wrapper
@dfunc
def test1():
    print('a')


if __name__ == '__main__':
    test()



'''
流程分析：

1 调用 test()
2 根据装饰器的概念，实际上调用的是 wrapper
3 f = func(*args) !重点注意：func（也就是test）函数包含yeild 返回的 f 是一个协程
    并不会立即执行。因此 print(start...) 并没有执行
4 print(1111...) 执行
5 print(2222...) 执行
6 print(3333...) 执行
7 print(result=None) 执行
8 a = f.send(result) 发送了None 且 协程test执行。
9 协程test() 输出 print(start...)
10 r = yield Async(add, (2, 3)) 
    Async() 只是记录了 add 函数 和参数。
    yield Async 对象返回给 f.send() 赋值给 a 继续执行。
11 print(4444...) 执行
12 apply_async(a.func, a.args, callback=result_queue.put)
    执行 result = a.func(a.args)，然后 result_queue.put(result)
    也就是执行的 add(2,3)  结果5 进入队列。
13 print(55555...) 执行，while True 继续。
14 print(1111...) 执行
15 result = result_queue.get()  result = 5
16 print(2222...) 执行
17 print(3333...) 执行
18 输出 result=5
19 a = f.send(5) 协程 test 继续之前的进度。
20 协程test yield 接收到5 返回给 r
21 输出 last=5, yield Async 对象给 send(5), a 获得 Async 对象。
22 print(4444...) 执行,
23 apply_async() 执行。把 helloworld 加入了队列。
24 print(5555...) 执行,
26 While True 继续执行，print(1111...) 执行,
27 result = 'helloword',print(2222...) 执行,
28 print(3333...) 执行, print('result=helloworld')
29 a = f.send(result) 协程test 继续之前的进度。
30 r 收到 result结果。 输出 last=helloword
31 输出 ====end====
32 主程序 test 退出。造成协程调度器中止。


'''