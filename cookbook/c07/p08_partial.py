#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 使用partial函数来减少参数个数
Desc : 

知识点：
    1 functools.partial 减少参数个数。也就是运行时预先设置默认值。
"""
import logging
from multiprocessing import Pool
from functools import partial
from socketserver import StreamRequestHandler, TCPServer


def spam(a, b, c, d):
    print(a, b, c, d)


def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)
        print(result)


# A sample function
def add(x, y):
    return x + y


class EchoHandler(StreamRequestHandler):
    # ack is added keyword-only argument. *args, **kwargs are
    # any normal parameters supplied (which are passed on)
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)




def test1():
    '''
    spam 函数 原本有4个参数，通过 partial 固定了一个参数的值，返回了一个新函数。

    pool.apply_async(func[, args[, kwds[, callback[, error_callback]]]])
    用进程池调用 func 函数（包括可选的args,kwds参数）
    callback 是一个回调函数，只有一个参数，是func执行的结果。    
    '''
    s1 = partial(spam, 1) # a = 1
    s1(2, 3, 4)
    s1(4, 5, 6)
    s2 = partial(spam, d=42) # d = 42
    s2(1, 2, 3)
    s2(4, 5, 5)
    s3 = partial(spam, 1, 2, d=42) # a = 1, b = 2, d = 42
    s3(3)
    s3(4)

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()

    # socket服务器
    serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
    serv.serve_forever()    


def test2():
    '''
    points 四个点的坐标，到 5.6,5.8 点的距离排序。
    通过 matplotlib 图示可以很容易看出距离。
    points.sort(key=) key 应该是一个函数，仅有一个参数。这个参数接收points 的每一个元素
    然后按照返回值进行排序。 这里通过 partial() 减少了 distance 的参数个数。返回了一个
    x 到 常数basepoint 的举例的回调函数。 就符合了 key 的要求。
    '''
    import math
    import numpy as np
    import matplotlib.pyplot as plt
    points = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
    
    def distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.hypot(x2 - x1, y2 - y1)    
    basepoint = (5.6,5.8)
    points.sort(key=partial(distance,basepoint))
    print(points)

    plt.axis([0,10,0,10])   # 设定坐标轴
    plt.axis('equal')       # 横纵坐标比例相等
    plt.grid(color='r',linestyle='dotted',alpha=.5) # 显示网格
    ps = np.array(points)   # 用numpy.array 保存二维数组，便于取值。
    plt.plot([5.6],[5.8],'ro',color='b')
    plt.plot(ps[:,0],ps[:,1],'ro')
    plt.show()




if __name__ == '__main__':
    test1()

