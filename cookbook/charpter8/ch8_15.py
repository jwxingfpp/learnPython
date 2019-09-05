# coding: utf-8
"""
@Time    : 2019/9/5 下午8:44
@Author  : xingjiawei

属性的代理访问
实现代理模式
"""


class Proxy(object):
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        return getattr(self._obj, item)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super(Proxy, self).__setattr__(key, value)
        else:
            print 'setattr', key, value
            setattr(self._obj, key, value)

    def __delattr__(self, item):
        if item.startswith('_'):
            super(Proxy, self).__delattr__(item)
        else:
            print 'delattr', item
            delattr(self._obj, item)


# 使用这个代理类时， 只需用它来包装下其他类
class Spam(object):
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print 'Spam.bar:', self.x, y


if __name__ == '__main__':
    s = Spam(2)
    p = Proxy(s)
    print p.x
    p.bar(5)
    p.y = 7
    print p.y