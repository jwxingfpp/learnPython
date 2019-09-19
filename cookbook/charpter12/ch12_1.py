# coding: utf-8
"""
@Time    : 2019/9/19 下午8:09
@Author  : xingjiawei
启动与停止线程
"""
import socket
import time
from threading import Thread


def print_n(n):
    print 'hello', n


class CountdownTask(object):
    def __init__(self):
        self._running = True

    # 增加信号，在特定点终止退出线程
    def terminate(self):
        self._running = False

    def running(self, n):
        while self._running and n > 0:
            print ('T-minus', n)
            n -= 1
            time.sleep(1)


if __name__ == '__main__':
    t1 = Thread(target=print_n, name='creat thread 1', args=(1,))
    t2 = Thread(target=print_n, name='creat thread 2', args=(2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    c = CountdownTask()
    t3 = Thread(target=c.running, args=(5, ))
    t3.start()
    c.terminate()
    t3.join()
