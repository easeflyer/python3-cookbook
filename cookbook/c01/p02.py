import numpy

'''
星号表达式：解压语法的灵活应用 



知识点：
  1 通过星号* 表达式，解压出 N 个元素。 N 代表不确定个数。
  2 numpy 的均值计算。 要使用 numpy 要先安装 Scipy

星号表达式：
扩展的迭代解压语法是专门为解压不确定个数或任意个数元素的可迭代对象而设计的。
'''

def avg(nums):
  return numpy.mean(nums)

def drop_first_last(grades):
    first, *middle, last = grades     # 注意 middle 得到一个列表
    return avg(middle)


scores = [0.1,1,2,3,4,5,6,7,8,9,10,99]

print("mean:",drop_first_last(scores))


# 例2
# 利用 星号表达式 存储后面不确定个数的数据。（电话号码）
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

print("name:",name)
print("email:",email)
print("phone_numbers:",phone_numbers)  # 注意 phone_numbers 得到一个列表


# 例3
# 比如，你有一个公司前 8 个月销售数据的序列， 但是你想看下最近一个月数据和前面 
# 7 个月的平均值的对比。你可以这样做：
# 输出结果可以看出。 最后一个月销售数据低于平均值

sales_record = [10, 8, 7, 1, 9, 5, 10, 3]

*trailing, current = sales_record
trailing_avg = sum(trailing) / len(trailing)
# return avg_comparison(trailing_avg, current)
print(trailing_avg)
print(current)


# trailing 尾随，随后。代表最后几个月
# comparison  n. 比较


# 例3 处理带标签的数据
# 注意 for tag, *args in records: 等同于下面的语法
# for (tag, *args) in records:
# 也是解压 语法的灵活应用。
print("例3 ==================")
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# 例4 处理字符串
'''
知识点：
  1 利用 split 分割字符串为列表
  2 利用星号表达式，隔离抽取出，开头和结尾的数据。
  3 注意 f 新语法 3.7.4 以上。

'''

print("例4 ==================")

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

print(f"uname:{uname}")
print(f"homedir:{homedir}")
print(f"sh:{sh}")

print(f"fields:{fields}")


# 例5  丢弃无用数据
'''
有时，我们想解压数据后，丢弃无用的数据。
利用 *_ 屏蔽丢弃的数据，可以 使得保留的数据看起来更加直观。
'''
print("例5 ==================")
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

print(f"name:{name} year:{year}")


# 例子6 实现递归算法
'''
知识点：
  1 if...else 三元表达式
'''



items = [1, 10, 7, 4, 5, 9]
head, *tail = items

print(f"head:{head} tail:{tail}")

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))

'''
三元运算的简易写法
'''
x,y = 3,4
if x > y:
  re = x
else:
  re = y

re1 = x if x<y else y
re2 = [x,y][x>y]

print(f"re:{re} re1:{re1} re2:{re2}")