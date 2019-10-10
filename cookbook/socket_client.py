# coding: utf-8
"""
@Time    : 2019/10/9 下午4:27
@Author  : xingjiawei
socket 客户端
"""
import socket

HOST = '127.0.0.1'
PORT = 65432


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        for i in range(5):
            data = raw_input()
            s.send(data)
            resp = s.recv(1024)
            print('server resp', resp.decode(encoding='utf-8'))
    finally:
        s.close()


if __name__ == '__main__':
    main()
