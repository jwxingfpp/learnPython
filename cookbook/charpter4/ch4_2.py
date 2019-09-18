# coding: utf-8
"""
@Time    : 2019/9/18 下午5:38
@Author  : xingjiawei
实现迭代器协议
Eg: 实现一个深度优先方式遍历树
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

    def depth_first(self):
        yield self
        for node in self._children:
            for n in node.depth_first():
                yield n


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
    c3 = Node(3)
    c4 = Node(4)
    root.add_children(c1)
    root.add_children(c2)
    c1.add_children(c3)
    c3.add_children(c4)
    for ch in root:
        print ch

    for i in frange(1, 10, 2):
        print i

    for node in root.depth_first():
        print node

