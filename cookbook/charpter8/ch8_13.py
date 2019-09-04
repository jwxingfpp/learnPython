# coding: utf-8
"""
@Time    : 2019/9/4 下午8:12
@Author  : xingjiawei
"""

# coding: utf-8
"""
@Time    : 2019/9/3 下午3:25
@Author  : xingjiawei
python 描述器
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


# Descriptor for enforcing types
class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expect {}'.format(self.expected_type))
        super(Typed, self).__set__(instance, value)


# Descriptor for enforcing values
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('need to be > 0')
        super(Unsigned, self).__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size')
        super(MaxSized, self).__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) > self.size:
            raise ValueError('value size must be < {}'.format(self.size))
        super(MaxSized, self).__set__(instance, value)


# 具体数据类型
class Integer(Typed):
    expected_type = int


class UnsignInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


# 上述类型约束采用类装饰器的方法
def check_attr(**kwargs):
    def wrapper(cls):
        for key, value in kwargs.iteritems():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls
    return wrapper


# 采用以上数据类型
@check_attr(name=SizedString(size=8),
            shares=UnsignInteger,
            price=UnsignFloat)
class Stock(object):
    # Specify constraints
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


if __name__ == '__main__':
    s = Stock('langsha', 1, 8.0)
    print s.__dict__
    print Stock.__dict__
    try:
        s.name = 's'*10
    except ValueError as e:
        print e

    try:
        s.price = 5
    except TypeError as e:
        print e

    try:
        s.shares = -1
    except ValueError as e:
        print e
