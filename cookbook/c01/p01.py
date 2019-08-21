'''
知识点：
    1 把一个特定数据结构，析构（解压） 到多个变量上。语法简单可读性好，代码量少。
    2 python3.7.4 字符串模板语法 f"{变量}"
    3 注意如果等号左右的结构不匹配，则会报错。
    4 事实上这种 解压，可以用在任何可迭代对象上面。

'''
p = (4,5)
x,y = p
print(x,y)

print("-"*80)

data = ['ACME',50,91.1,(2012,12,21)]
name, shares, price, date = data
print(f"date:{date} name:{name}")
name, shares, price, (year, month, day) = data
print(f"year:{year} month:{month} day:{day}")