# coding: utf-8
"""
@Time    : 2019/8/8 上午9:57
@Author  : xingjiawei
---------------------------
python赋值机制
"""

def new_print(x):
    print 'value assign to:{}'.format(id(x))


def print_seperator():
    print '-'*20


def print_info(s1, s2):
    new_print(s1)
    new_print(s2)
    print s1 is s2
    print_seperator()


def main():
    # 不可变变量
    x = 123
    y = x       # 此时，系统并没有为y分配内存，而是指向123的内存地址
    print_info(x, y)

    # y重新赋值，会产生新内存
    y = 234
    print_info(x, y)

    s1 = 'lalala'
    s2 = s1
    print_info(s1, s2)

    # 同理, s2也是
    s2 = 'ha'*3
    print_info(s1, s2)

    ##########################
    # 可变 list
    l1 = range(1, 4)
    l2 = l1
    print_info(l1, l2)
    l2[0] = 4
    print_info(l1, l2)
    print_info(l1[0], l2[0])


if __name__ == '__main__':
    main()
