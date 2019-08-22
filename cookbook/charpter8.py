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

    def __enter__(self):
        """上下文管理"""
        """当调用with语句时，该函数返回值赋值给as后的变量"""
        print 'entering'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'exiting'
        if exc_val:
            print 'exc err, type:{}, err:{}'.format(exc_type, exc_val)

    def aver_score(self):
        raise Exception('no score')


if __name__ == '__main__':
    stu = Student('xjw', 16, 'M')
    print stu

    with Student('jj', 14, 'f') as s:
        print s
        s.aver_score()

