'''
python3 -m http.server 15000

>>> from urllib.request import urlopen
>>> u = urlopen('http://localhost:15000/fib.py')
>>> data = u.read().decode('utf-8')
>>> print(data)
# fib.py
print("I'm fib")
def fib(n):
if n < 2:
return 1
else:
return fib(n-1) + fib(n-2)
>>
'''


print("I'm fib")
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)