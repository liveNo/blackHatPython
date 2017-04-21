#!/bin/python
# -*- coding=utf-8 -*-
from IPy import IP

# IP地址/网段的基本处理

#1. 通过version方法可以区分是Ipv4还是IPv6

print IP('10.0.0.0/8').version()
print IP('::1').version()


# 2. 通过指定的网段输出该网段的IP个数及所有IP地址清单
ip = IP('192.168.0.0/16')
print ip.len()

# 3. IP类几个常见的方法
ip = IP('192.168.1.20')
print ip.reverseNames() # 反向解析地址格式

print ip.iptype()  # 网络类型

print IP('8.8.8.8').int() # 转换成整型格式
print IP('8.8.8.8').strHex()  # 转换成十六进制格式
print IP('8.8.8.8').strBin()  # 转换成二进制格式
print IP(0x8080808) # 十六进制转成IP格式

# IP方法也支持网络地址的转换,例如根据IP与掩码生产网段格式

print IP('192.168.1.0').make_net('255.255.255.0')
print IP('192.168.1.0/255.255.255.0', make_net=True)
print IP('192.168.1.0-192.168.1.255', make_net=True)