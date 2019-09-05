# coding: utf-8
"""
@Time    : 2019/9/5 下午8:44
@Author  : xingjiawei

属性的代理访问
代理是一种编程模式, 目的可能是作为继承的一个替代方法或者实现代理模式
"""
class A:
    def spam(self, x):
        print 'A spam running'
        print x

    def foo(self):
        print 'A foo running'


class B:
    def __init__(self):
        self._a = A()

    # Expose all of the methos defined on class A
    def __getattr__(self, item):
        """
        这个方法在访问的attribute不存在的时候被调用
        """
        return getattr(self._a, item)


if __name__ == '__main__':
    b = B()
    b.spam(1)
    b.foo()