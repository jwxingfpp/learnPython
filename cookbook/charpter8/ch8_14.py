# coding: utf-8
"""
@Time    : 2019/9/5 下午8:14
@Author  : xingjiawei
实现自定义容器
"""

import collections


class List(collections.Iterable):
    def __init__(self):
        self.children = range(1, 6)

    def __iter__(self):
        return iter(self.children)


if __name__ == '__main__':
    l = List()
    for a in l:
        print a
