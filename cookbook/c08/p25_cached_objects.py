#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 创建缓存实例
Desc :
"""

import logging

def test1():
    a = logging.getLogger('foo')
    b = logging.getLogger('bar')
    print(a is b)
    c = logging.getLogger('foo')
    print(a is c)

# The class in question
class Spam:
    def __init__(self, name):
        self.name = name

# Caching support
import weakref

_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s

def test11():
    '''
    1 spam 对象的创建通过 get_spam 代理。
    2 get_spam 首先判断 同名 spam 是否已经存在，如果存在就返回，不存在则新建，并缓存。
    3 这里用了弱引用，缓存对于对象的弱引用，保证了不会影响到其他逻辑对对象的 删除操作。
        当其他引用删除了对对象的引用。则对象内存被回收，缓存失效。
    '''

    a = get_spam('foo')
    b = get_spam('bar')
    c = get_spam('foo')

    print(f"a is b:{a is b}")
    print(f"a is c:{a is c}")
    



# Note: This code doesn't quite work
class Spam1:
    '''
    注意这里 __new__ 虽然设计良好，貌似可以实现缓存。
    但是 __init__ 每次都被执行了。也就是说 self.name 每次都被重新赋值。
    而不是从缓存中取出的。这不是预期的效果。
    '''
    _spam_cache = weakref.WeakValueDictionary()

    def __new__(cls, name):
        print('Spam1__new__')
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self

    def __init__(self, name):
        print('Initializing Spam')
        self.name = name


def test2():
    s = Spam1('Dave')
    t = Spam1('Dave')
    print(f"s is t:{s is t}")

class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s

    def clear(self):
        self._cache.clear()


class Spam2:
    manager = CachedSpamManager()

    def __init__(self, name):
        self.name = name

def get_spam(name):
    return Spam2.manager.get_spam(name)


# ------------------------最后的修正方案------------------------
class CachedSpamManager2:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            temp = Spam3._new(name)  # Modified creation
            self._cache[name] = temp
        else:
            temp = self._cache[name]
        return temp

    def clear(self):
        self._cache.clear()


class Spam3:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")

    # Alternate constructor
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self

def test3():
    print('------------------------------')
    cachedSpamManager = CachedSpamManager2()
    s = cachedSpamManager.get_spam('Dave')
    t = cachedSpamManager.get_spam('Dave')
    print(s is t)


test1()
test11()
test2()
test3()