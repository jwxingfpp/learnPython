# coding: utf-8
"""
@Time    : 2019/9/25 下午5:39
@Author  : xingjiawei
描述器
"""


# Base class Descriptor
class Descriptor(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner=None):
        print 'ins: ', instance, instance.__dict__
        value = instance.__dict__.get(self.name, 'oops')
        return value

    def __set__(self, instance, value):
        print 'set value'
        instance.__dict__[self.name] = value


####################################
# 通过类及继承实现描述器
####################################
# Typed class
class Typed(Descriptor):
    expect_type = None

    def __set__(self, instance, value):
        if not isinstance(value, self.expect_type):
            raise TypeError('type must be ', self.expect_type)
        super(Typed, self).__set__(instance, value)


# maxsized class
class MaxSized(Descriptor):
    def __init__(self, name, max_len):
        self.name = name
        self.max_len = max_len

    def __set__(self, instance, value):
        if len(value) > self.max_len:
            raise ValueError('length must be < ', self.max_len)
        super(MaxSized, self).__set__(instance, value)


# Unsigned class
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('must be > 0')
        super(Unsigned, self).__set__(instance, value)


class Float(Typed):
    expect_type = float


class String(MaxSized, Typed):
    expect_type = str


class Int(Typed):
    expect_type = int


class UnsignedFloat(Float, Unsigned):
    pass


class UnsignedInt(Int, Unsigned):
    pass


###################################
# 使用类装饰器实现描述器
###################################
def unsigned(cls):
    cls_set = cls.__set__

    # set
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('must be > 0')
        cls_set(self, instance, value)

    cls.__set__ = __set__
    return cls


def typed(expect_type, cls):
    cls_set = cls.__set__

    def __set__(self, instance, value):
        if not isinstance(value, expect_type):
            raise TypeError('must be ', expect_type)
        cls_set(self, instance, value)
    cls.__set__ = __set__

    return cls


class Str(Descriptor):
    pass


@unsigned
class unsigedInt(Int):
    pass


class Stock(object):
    price = UnsignedFloat('price')
    shares = UnsignedInt('shares')
    name = String('name', 10)
    # factory = typed(str, Str)('factory')

    def __init__(self, price, shares, name):
        self.price = price
        self.shares = shares
        self.name = name


######################################
# 通过元类实现
######################################
class MetaClass(type):
    def __new__(cls, clsname, bases, kwargs):
        for k, v in kwargs.items():
            print 'meta class, ', k, v
            if isinstance(v, Descriptor):
                v.name = k
        cls_ins = type.__new__(cls, clsname, bases, kwargs)
        print type(cls_ins), cls_ins, cls_ins.__name__, cls_ins.__dict__
        return cls_ins


class Stock1(object):
    __metaclass__ = MetaClass
    name = String('name', 10)
    price = UnsignedFloat('price')
    shares = unsigedInt('shares')


if __name__ == '__main__':
    # 类实现描述器
    s = Stock(4.5, 12, 'langsha')
    print s.__class__.__dict__
    print s.__dict__
    # 类装饰器实现描述器
    Stock.factory = typed(str, Str)('factory')
    s.factory = 'dd'
    print s.__dict__
    Stock.num = unsigedInt('num')
    s.num = 1
    print s.__dict__

    # 元类
    s = Stock1()
    s.name = 'www'

