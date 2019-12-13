#!/usr/bin/env python
# -*- encoding: utf-8 -*-



'''
描述符案例2

对于描述符基本理解：
    1 优先级：
        应明确属性查询优先级。
    2 数据描述符，优先于实力属性：
        因为 数据描述符 优先于实例属性。因此对 td.y 的访问会被描述符__get__ 处理。
    3 同名实例属性被替代：
        对象实例如果设置了 和 数据描述符同名属性，将会被替代且删除这个属性。
    4 self.属性名也遵循优先级：
        如果有同名数据描述符，则self.属性名 访问的也是数据描述符，而非实例属性
    5 TestDesc.y,td.y 都被__get__代理。
        只有 TestDesc.__dict__['y']才是真实的 Desc 对象。
    6 描述符属性，只能定义为类属性，不能定义为实例属性。

    7 访问 td.y:  __get__(self,td实例,TestDesc)
      访问 TestDesc.y: __get__(self,None,TestDesc)
'''





class Desc():
    def __init__(self,v):
        self._v = v
    def __get__(self, instance, cls):
        print('Desc.__get__():')
        print('instance:{},cls:{}'.format(instance,cls))
        return self._v
    def __set__(self, instance, value):
        print('Desc.__set__():')
        self._v = value



class TestDesc():
    '''
    '''
    x = 2
    y = Desc(0)
    z = 4
    def __init__(self):
        self.x = 20
        print("init self.y:",self.y)
        self.y = 30  # 这里的 ye
        self.z = 40


if __name__ == '__main__':
    import pdb;pdb.set_trace()
    td = TestDesc()
    print('td.__dict__:',td.__dict__)
    # td.__dict__: {'x': 20} 没有 y 
    print('TestDesc.__dict__',TestDesc.__dict__)
    # 包含 x 和 y x 和 self.x 不是一个变量。
    print('TestDesc.__dict__[x]:',TestDesc.__dict__['x'])
    # 
    print('td.__dict__[x]:',td.__dict__['x'])
    # print('td.__dict__[y]:',td.__dict__['y']) 报错。因为 y 按照访问顺序，无法读取，因此
    # python 内部规则把他去掉了。因为有了 “描述符”变量 y