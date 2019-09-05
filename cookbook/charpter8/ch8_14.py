# coding: utf-8
"""
@Time    : 2019/9/5 下午8:14
@Author  : xingjiawei
实现自定义容器
"""
import bisect
import collections


# 继承Sequence抽象类，并且实现元素按照顺序存储
class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding item in the right location
    def add(self, item):
        bisect.insort(self._items, item)


if __name__ == '__main__':
    s = SortedItems(range(2, 5))
    print s
    print list(s)
    print s[0], s[-1]
    s.add(5)
    print list(s)
    print '-'*10
    print isinstance(s, collections.Sequence)
    print isinstance(s, collections.Iterable)
    print isinstance(s, collections.Container)
    print isinstance(s, collections.Sized)
