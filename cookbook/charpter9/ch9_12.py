# coding: utf-8
"""
@Time    : 2019/9/17 上午9:39
@Author  : xingjiawei
使用装饰器扩充类的功能
"""


def log_getattribute(cls):
    orig_getattribute = cls.__getattribute__

    # Make a new definition
    def new_getattribute(self, name):
        print 'getting {}'.format(name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = new_getattribute
    return cls


# Example use
@log_getattribute
class A(object):
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


# 另种方案就是使用继承实现以上功能
# 使用此方案必须了解方法调用顺序、super以及继承
# 而使用类装饰器则更加直观，运行速度更快一些
class LoggedGetattribute(object):
    def __getattribute__(self, name):
        print 'getting {}'.format(name)
        return super(LoggedGetattribute, self).__getattribute__(name)


class B(LoggedGetattribute):
    def __init__(self, x):
        self.x = x


if __name__ == '__main__':
    a = A(42)
    print a.x

    b = B(43)
    print b.x
