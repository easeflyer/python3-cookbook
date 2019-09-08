#!/usr/bin/env python
# -*- encoding: utf-8 -*-



'''
描述符案例2

对于描述符基本理解：

'''





class Desc():
    def __init__(self,v):
        self._v = v
    def __get__(self, instance, cls):
        print('Desc.__get__():')
        return self._v
    def __set__(self, instance, value):
        print('Desc.__set__():')
        self._v = value



class TestDesc():
    '''
    '''
    x = 2
    y = Desc(0)
    def __init__(self):
        self.x = 20
        self.y = 30


if __name__ == '__main__':
    import pdb;pdb.set_trace()
    td = TestDesc()
    print(33)
    print(44)