# coding:utf-8
"""
生成器需要实现__iter__和next(python2), __next__(Python3)
可迭代(for)需实现 __iter__， return self
"""


class Fib(object):
    def __init__(self, n):
        self.prev = 0
        self.cur = 1
        self.n = n

    # 需要使用for的话，对象必须是iterable,
    # 必须实现__iter__() 或 __getitem__()
    def __iter__(self):
        return self

    # 迭代器必须实现next (Python2), __next__ (Python3)
    def next(self):
        if self.n > 0:
            value = self.cur
            self.prev, self.cur = self.cur, self.cur+self.prev
            self.n -= 1
            return value
        else:
            raise StopIteration()


if __name__ == '__main__':
    fib = Fib(5)
    for i in fib:
        print i
