# coding: utf-8
"""
@Time    : 2019/9/18 下午5:38
@Author  : xingjiawei
代理迭代
Q: 构建自定义容器对象，需要在该容器对象上执行迭代操作
"""


class Node(object):
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_children(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


# 生成器迭代
def frange(start, end, increment):
    x = start
    while x < end:
        yield x
        x = x + increment


if __name__ == '__main__':
    root = Node(0)
    c1 = Node(1)
    c2 = Node(2)
    root.add_children(c1)
    root.add_children(c2)

    for ch in root:
        print ch

    for i in frange(1, 10, 2):
        print i

