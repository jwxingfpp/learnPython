# coding: utf-8
"""
@Time    : 2019/8/28 下午9:11
@Author  : xingjiawei

简化数据结构的初始化
Q: 写很多仅仅用作数据结构的类，不想写太多烦人的__init__() 函数
"""
import math


class BaseStruct:
    """class viriable that specifies expected fields"""
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise AttributeError('Expect {} args', len(self._fields))
        # set the arguments
        for key, value in zip(self._fields, args):
            setattr(self, key, value)


# example class definations
class Triangle(BaseStruct):
    _fields = ['bottom', 'height']

    # TODO 统一接口
    @property
    def area(self):
        return self.bottom * self.height * 0.5


class Rectangle(BaseStruct):
    _fields = ['width', 'length']

    @property
    def area(self):
        return self.width * self.length


class Circle(BaseStruct):
    _fields = ['radius']

    @property
    def area(self):
        return math.pi * self.radius**2


if __name__ == '__main__':
    t = Triangle(3, 5)
    r = Rectangle(2, 4)
    c = Circle(4)

    print t.__dict__, r.__dict__, c.__dict__
    print t.bottom
    print t.area
    print c.area