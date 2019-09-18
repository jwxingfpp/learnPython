# coding: utf-8
"""
@Time    : 2019/9/18 下午2:12
@Author  : xingjiawei
带额外状态信息的回调函数
"""


def print_result(result):
    print 'got', result


def add(x, y):
    return x + y


def apply_async(func, call_back, *args):
    r = func(*args)
    call_back(r)


class ResultHandler(object):
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print '[{}] Got: {}'.format(self.sequence, result)


# 闭包
def make_handler():
    sequence = [0]

    def handler(result):
        sequence[0] += 1
        print '[{}] Got: {}'.format(sequence[0], result)
    return handler


# 协程
def make_handler1():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print '[{}] Got: {}'.format(sequence, result)


if __name__ == '__main__':
    apply_async(add, print_result, 1, 2)
    apply_async(add, print_result, 'hello', 'world')

    # 使用类
    rh = ResultHandler()
    apply_async(add, rh.handler, 1, 2)
    apply_async(add, rh.handler, 'hello', 'world')

    # 闭包
    handler = make_handler()
    apply_async(add, handler, 1, 2)
    apply_async(add, handler, 'hello', 'world')

    # 协程
    handle = make_handler1()
    next(handle) # advance to the yield
    apply_async(add, handle.send, 1, 2)
    apply_async(add, handle.send, 'hello', 'world')
