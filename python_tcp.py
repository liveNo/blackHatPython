# coding=utf-8
#/usr/bin/python

import socket

target_host = "127.0.0.1"
target_port = 9999

# 建立一个socket 连接
# 建立一个包含AF_INET和SOCK_STREAM参数的socket对象。AF_INET 参数说明我们将使用标准的IPv4地址或者主机名，SOCK_STREAM说明这将是一个TCP客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接客户端
client.connect((target_host, target_port))

# 发送一些数据
client.send("GET / HTTP/1.1\r\nHost:baidu.com\r\n\r\n")

# 接收一些数据
response = client.recv(4096)

print response


