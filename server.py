#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import requests
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
sk.bind(ip_port)
sk.listen(5)

#读取文件
fp = open("auth.conf", "w+")
auth_dict = {}
for line in fp:
    auth_name = line.split()[0]
    auth_pwd = line.split()[1]
    auth_dict[auth_name] = auth_pwd

stored_data = {}
return_data = ""
auth_flag = False
url_dict = {}
print 'server waiting...'
conn, addr = sk.accept()
while True:
    client_data = conn.recv(1024)
    print client_data
    client_dataarr = client_data.split()
    if client_dataarr[0].upper() == "SET":
        print client_dataarr[0],client_dataarr[1],client_dataarr[2]
        stored_data[client_dataarr[1]] = client_dataarr[2]
        print stored_data
    elif client_dataarr[0].upper() == "GET":
        if client_dataarr[1] in stored_data.keys():
            return_data = stored_data[client_dataarr[1]]
        else:
            return_data = "none"
        conn.sendall(return_data)
    elif client_dataarr[0].upper() == "AUTH":
        if client_dataarr[1] in auth_dict.keys():
            if client_dataarr[2] == auth_dict[client_dataarr[1]]:
                auth_flag = True
                conn.sendall("1")
            else:
                auth_flag = False
                conn.sendall("0")
        else:
            auth_flag = False
            conn.sendall("0")
    elif client_dataarr[0].upper() == "URL":
        if client_dataarr[1] in url_dict.keys():
            inner_arr = url_dict[client_dataarr[1]]
            conn.sendall(inner_arr[0] + " " + inner_arr[1])
        else:
            html = requests.head(client_dataarr[2])
            res_code = html.status_code
            res_length = html.headers.get('Content-Length')
            url_dict[client_dataarr[1]] = [res_code, res_length]
            conn.sendall("none")


conn.close()
