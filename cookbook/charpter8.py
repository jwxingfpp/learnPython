# coding: utf-8
"""
@Time    : 2019/8/21 下午8:35
@Author  : xingjiawei
"""


class Student(object):
    def __init__(self, name, age, gendor):
        self.name = name
        self.age = age
        self.gendor = gendor

    def __repr__(self):
        """print self"""
        return "instance of {}, and name is:{}, age:{}, gendor:{}".format(self.__class__.__name__, self.name,
                                                                          self.age, self.gendor)


if __name__ == '__main__':
    stu = Student('xjw', 16, 'M')
    print stu
