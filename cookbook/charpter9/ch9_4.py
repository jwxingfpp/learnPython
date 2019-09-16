# coding: utf-8
"""
@Time    : 2019/9/16 上午10:08
@Author  : xingjiawei
装饰器添加参数
"""
import logging
from functools import wraps


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.info(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


@logged(logging.DEBUG)
def count(n):
    for i in range(n):
        pass


if __name__ == '__main__':
    # 装饰器
    count(15)
    print count