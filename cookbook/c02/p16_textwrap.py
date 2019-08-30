#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 格式化字符串为指定宽度
Desc : 

    知识点：
        1 textwrap 的使用。
        2 处理中文 需要把字符数除以2
"""
import textwrap
import os


def reformat_width():
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under. Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under.Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under.Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under."

    scn = "sub() 函数使用 sys._getframe(1) 返回调用者的栈帧。可以从中访问属性 \
    f_locals 来获得局部变量。毫无疑问绝大部分情况下在代码中去直接操作栈帧应 \
    该是不推荐的。但是，对于像字符串替换工具函数而言它是非常有用的。另外，值得注 \
    意的是 f_locals 是一个复制调用函数的本地变量的字典。尽管你可以改变 f_locals \
    的内容，但是这个修改对于后面的变量访问没有任何影响。所以，虽说访问一个栈帧看 \
    上去很邪恶，但是对它的任何操作不会覆盖和改变调用者本地变量的值。" 

    print(textwrap.fill(s, 70))
    print('*' * 40)
    print(textwrap.fill(s, 40))
    print('*' * 40)
    print(textwrap.fill(s, 40, initial_indent='_'*4))       # 第一行开头加缩进。
    print('*' * 40)
    print(textwrap.fill(s, 40, subsequent_indent='_'*4))    # 第二行开始加缩进

    # 获取终端屏幕尺寸
    print(os.get_terminal_size().columns)


if __name__ == '__main__':
    reformat_width()