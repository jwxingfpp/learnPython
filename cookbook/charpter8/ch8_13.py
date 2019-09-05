# coding: utf-8
"""
@Time    : 2019/9/4 下午8:12
@Author  : xingjiawei

采用装饰器替代之前定义的类，效果一样
但执行速度更快
"""


# Base class, use a descriptor to set a value
class Descriptor(object):
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.iteritems():
            setattr(self, key, value)

    def __get__(self, instance, owner):
        print 'call __get__'
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print 'call __set__'
        instance.__dict__[self.name] = value


# 使用装饰器代理混入类
# Decorator for applying type checking
def Typed(expected_type, cls=None):
    if cls is None:
        return lambda cls: Typed(expected_type, cls)

    cls_set = cls.__set__

    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError('expect {}'.format(expected_type))
        cls_set(self, instance, value)
    cls.__set__ = __set__
    return cls


# Decorator for unsigned values
def Unsigned(cls):
    cls_set = cls.__set__

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('must be > 0')
        cls_set(self, instance, value)
    cls.__set__ = __set__
    return cls


# decrator for allowing sized values
def MaxSized(cls):
    cls_init = cls.__init__

    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size')
        cls_init(self, name, **opts)

    cls.__init__ = __init__
    cls_set = cls.__set__

    def __set__(self, instance, value):
        if len(value) > self.size:
            raise ValueError('must be < {}'.format(self.size))
        cls_set(self, instance, value)
    cls.__set__ = __set__
    return cls


# Specialized descriptors
@Typed(int)
class Integer(Descriptor):
    pass


@Unsigned
class UnsignedInt(Integer):
    pass


@Typed(float)
class Float(Descriptor):
    pass


@Unsigned
class UnsignedFloat(Float):
    pass


@Typed(str)
class String(Descriptor):
    pass


@MaxSized
class SizedString(String):
    pass


class Stock(object):
    name = SizedString('name', size=8)
    shares = UnsignedInt('shares')
    price = UnsignedFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


if __name__ == '__main__':
    s = Stock('langsha', 1, 8.0)
    print s.__dict__
    print Stock.__dict__
    print s.name
    print s.shares
    print s.price

    try:
        s.name = 'h'*10
    except ValueError as e:
        print e

    try:
        s.shares = -1
    except ValueError as e:
        print e

    try:
        s.price = 1
    except TypeError as e:
        print e