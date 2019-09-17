# coding: utf-8
"""
@Time    : 2019/9/16 上午9:36
@Author  : xingjiawei
装饰器
增加额外操作（如日志、计时等）
"""
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print '='*10, func.__name__, ' cost=', end-start
        return result
    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


def count(n):
    for i in range(n):
        pass


class A(object):
    @timethis
    def countdown(self, n):
        print '-'*10, 'instance countdown'
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def count(cls, n):
        print '-'*10, 'class method'
        while n > 0:
            n -= 1


if __name__ == '__main__':
    # 装饰器
    countdown(15)
    # 函数作为参数传入
    wrapper_count = timethis(count)
    wrapper_count(15)
    print countdown
    print wrapper_count

    a = A()
    a.countdown(15)
    A.count(15)
