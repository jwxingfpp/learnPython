# coding: utf-8
"""
@Time    : 2019/8/14 上午9:56
@Author  : xingjiawei
生成器
"""


def fib(n):
    a, b = 1, 1
    while n > 0:
        n -= 1
        yield a
        a, b = a+b, a


if __name__ == '__main__':
    gen = fib(5)
    for g in gen:
        print g

