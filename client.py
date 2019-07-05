#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import getopt
import sys

opts, args = getopt.gnu_getopt(sys.argv[1:], '', ['host=', 'port='])
ip = '127.0.0.1'
port = 5678
for opt, arg in opts:
    if opt in ('--host'):
        ip = arg
    if opt in ('--port'):
        port = arg


ip_port = (ip, port)
sk = socket.socket()
sk.connect(ip_port)
user_input = raw_input("请输入指令")
while user_input != "quit":
    sk.sendall(user_input)
    if user_input.startswith("set"):
        pass
    else:
        server_reply = sk.recv(1024)
        print server_reply
    # sk.close()
    # sk.connect(ip_port)
    user_input = raw_input("请输入指令")

# sk.sendall('请求占领地球 aa bb')
# sk.sendall("\nnihao")

# server_reply = sk.recv(1024)
# print server_reply
sk.close()


# 123

# ffff

# local
# local2
#local3
#remote

# remote2
# aaaa


#23123
# remote 3

<<<<<<< HEAD
>>>>>>> e8b9200ea31c61c5856bc291039127777985c5f0

# local 3
=======
# 123456
>>>>>>> 3c9a241b91ff72a4663f4b60b398ccf3ea9ffc98

# loca;4
