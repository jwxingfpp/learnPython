# coding: utf-8
"""
@Time    : 2019/9/18 下午3:51
@Author  : xingjiawei
协程
"""
"""
协程通过yield、send来进行控制程序
首先，产生生成器(h())
其次，调用next(h())，开始执行流程，其中第一次next 约等同于 send(None)
然后，send(msg)，将msg赋值与yield左侧
直至，StopIteration
"""


def h():
    print 'la'*5
    # 首先执行yield 2， 将2返回
    # 下个next将send(msg)中，msg赋值于m
    m = yield 2
    print 'got m', m


def f():
    a = None
    c = h()
    while True:
        try:
            # 第一次send(None), 作用相当于next，进入生成器迭代，并将yield 返回内容赋值于a
            # 下个循环，将最新的a发送，赋值于m
            # 直至StopIteration
            a = c.send(a)
            print a
            a += 2
        except StopIteration as e:
            print 'generator stop, ', repr(e)
            break


if __name__ == '__main__':
    f()