# coding: utf-8
"""
@Time    : 2019/9/17 上午9:55
@Author  : xingjiawei
使用元类
"""


class MetaClass(type):
    def __call__(self, *args, **kwargs):
        raise TypeError('can\'t instantiate directly')


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(*args, **kwargs)
            return self.__instance
        return self.__instance


class Singleton1(object):
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = super(Singleton1, cls).__new__(cls, *args, **kwargs)
            print cls._singleton
        return cls._singleton


# Example
class Spam(object):
    __metaclass__ = MetaClass

    @staticmethod
    def grok(x):
        print 'Spam.grok'


# singleton example
class Bar(object):
    __metaclass__ = Singleton

    def __init__(self):
        print 'creating single bar'


if __name__ == '__main__':
    Spam.grok(42)
    # s = Spam()
    # s.grok(42)

    b = Bar()
    b1 = Bar()
    print id(b)
    print id(b1)
    print b == b1

    b2 = Singleton1()
    b3 = Singleton1()
    print b2 is b3
