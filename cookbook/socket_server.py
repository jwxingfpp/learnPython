# coding: utf-8
"""
@Time    : 2019/9/27 下午6:43
@Author  : xingjiawei
socket编程，服务端
"""
import socket
import threading
from threading import Thread

HOST = '127.0.0.1'
PORT = 65432


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(1)

        while True:
            conn, addr = s.accept()
            print ('connect succ, addr:', addr)
            t = Thread(target=msg_handle, args=(conn, ))
            t.setDaemon(True)
            t.start()
    finally:
        s.close()


def msg_handle(conn):
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print ('msg from client', data.decode(encoding='utf-8'))
            conn.sendall(data)
    finally:
        conn.close()


if __name__ == '__main__':
    main()


