'''
本例目的：
    实践通过 __dict__.update 添加属性 和 setattr() 函数添加有什么不同。


知识点：
    1 __slots__ 使用元组定义，限制的是“当前类”“实例”的属性。并不限制类属性的添加。
    2 设置了 __slots__ 后，Structure 的 __init__  中 self.__dict__.update 就不起作用了?
        进过测试 s1.__dict__['name'] 依然存在，但是 s1.name 无法读取提示：AttributeError: name
    
总结：
    通过 __dict__.update 来实现并不通用。不如用 setattr() 是python 内部机制使然。
'''


class Structure:
    # Class variable that specifies expected fields
    _fields= []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments (alternate)
        import pdb;pdb.set_trace()
        self.__dict__.update(zip(self._fields,args))
        aaa = 333


class Stock(Structure):
    __slots__ = ('name','shares','price')
    _fields=['name','shares','price']

def test1():
    s1 = Stock('appl',21,520.1)
    s1.cname = "姓名"
    print(f"s1.name:{s1.name} s1.shares:{s1.shares} s1.price:{s1.price}")
    print(f"s1.cname:{s1.cname}")


# ------__slots__ 案例 ---------
'''
注意 如果 Student 继承 Stu 则仅对 Student 增加 __slots__ 并不能限制对象添加属性。
只有对父类同时添加 __slots__ 才可以限制。同样只对父类添加，子类不添加也不行。
'''


class Stu:
    __slots__ = ('name1','study1') # 只限制实例属性只能有 name 和 study
    cname = 'Stu'

class Student(Stu):
    __slots__ = ('name1','study1') # 只限制实例属性只能有 name 和 study
    cname = 'Student'
def study():
    print('I am studying!')

def test2():
    s1 = Student()
    s1.name = "张三"
    s1.study = study
    s1.study()
    Student.cname = "姓名"
    print(s1.cname)
# ------__slots__ 案例 ---------







if __name__ == '__main__':
    test1()  # 子类属性被正确建立。
    #test2()