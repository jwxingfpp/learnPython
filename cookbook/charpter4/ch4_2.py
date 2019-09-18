# coding: utf-8
"""
@Time    : 2019/9/18 下午5:38
@Author  : xingjiawei
实现迭代器协议
Eg: 实现一个深度优先方式遍历树
"""
from itertools import islice, permutations, combinations

"""
迭代协议要求一个__iter__()方法返回一个特殊的迭代器对象，该迭代器对象实现了__next__()方法
并通过StopIteration异常表示迭代的完成
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


def count(n):
    while True:
        yield n
        n += 1


# 展开嵌套序列
def flat(items):
    for x in items:
        if isinstance(x, list):
            for x1 in flat(x):
                yield x1
        else:
            yield x


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

    c = count(0)
    for x in islice(c, 10, 21):
        print x

    a = ['a', 'b', 'c']
    # 所有排列
    for x in permutations(a):
        print x

    # 不同元素的排列
    for x in permutations(a, 2):
        print x

    # 不同元素组合
    for x in combinations(a, 2):
        print x

    # 序号及内容
    for index, value in enumerate(a):
        print index, value

    # 合并连个列表
    b = range(1, 4)
    print type(zip(b, a)), zip(b, a)
    for index, value in zip(b, a):
        print index, value

    items = [1, 2, [3, 4, [5, 6], 7], 8]
    for i in flat(items):
        print i
