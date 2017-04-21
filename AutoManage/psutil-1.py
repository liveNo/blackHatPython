#!/bin/python
# -*- coding=utf-8 -*-

import psutil
import datetime

"""
  CPU 信息
  CPU利用率包含:
  1. User Time 执行用户进程的时间百分比
  2. System Time  执行内核进程和中断的时间百分比
  3.Wait IO,由于等待而使CPU牌=处于idle(空闲)状态的时间百分比
"""

print psutil.cpu_times()

print "CPU Percent ========="
for x in range(3):
    print psutil.cpu_percent(interval=1)


print "CPU Percent ==========="
for x in range(3):
    print psutil.cpu_percent(interval=1, percpu=True)

print "CPU Times percent ========"
for x in range(3):
    print psutil.cpu_times_percent(interval=1, percpu=False)

print "Cpu count ====="
print psutil.cpu_count()  # 获取CPU的逻辑个数,默认logical=True
print psutil.cpu_count(logical=False) # 获取CPU的物理个数

"""
  内存信息
  Linux 系统内存的利用率信息涉及total(内存数据), used(已使用的内存数), free(空闲内存数),buffers(缓冲使用数), cache(缓存使用数),
  swap(交换分区使用数)等, 分别使用psutil.virtual_memory()与 psutil.swap_memory()方法获取这些信息.
"""

# 使用psutil.virtual_memory 方法获取内存完整信息
mem = psutil.virtual_memory()

print mem.total  # 获取内存总数
print mem.free # 获取空闲内存数

# 获取SWAP分区信息
print psutil.swap_memory()

"""
 磁盘信息
 在系统的所有磁盘信息中,我们更加关注磁盘的利用率及IO信息,其中磁盘利用率使用psutil.disk_usage方法获取.磁盘IO信息包括read_count(读IO数),
 write_count(写IO数), read_bytes(IO读字节数), write_bytes(IO写字节数),read_time(磁盘读时间),wirte_time(磁盘写时间)等.
"""
# 使用psutil.disk_partitions 方法获取磁盘完整信息
print psutil.disk_partitions()

# 使用psutil.disk_usage方法获取分区(参数)的使用情况
print psutil.disk_usage('/home/xuyanlu')

# 使用psutil.disk_io_counter 获取硬盘总的IO个数
print psutil.disk_io_counters()

print psutil.disk_io_counters(perdisk=True)

"""
 网络信息
 系统的网络信息与磁盘IO类似,涉及几个关键点,包括bytes_sent(发送字节数), bytes_recv=28220119(接收字节数),packets_sent=200978(发送数据包数)
 packets_recv=212673(接收数据包数)等.
"""

# 使用psutil.net_io_counters获取网络总的IO信息,默认pernic=False
print psutil.net_io_counters()

# pernic=True 输出每个网络接口的IO信息
print psutil.net_io_counters(pernic=True)

"""
 其他系统信息
"""
# 使用psutil.users方法返回当前登录系统的用户信息
print psutil.users()

# 使用psutil.boot_time方法获取开机时间,以Linux时间戳格式返回
print psutil.boot_time()

# 转换成自然时间格式
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d")

"""
 进程管理
"""
pids = psutil.pids()
print pids

p = psutil.Process(14073);
print p.name()
# print p.exe()
# print p.cwd()
print p.cmdline()

print p.pid
print p.ppid()

print p.parent()

print p.children()

print p.status()

print p.username()
print p.create_time()

print p.terminal()
print p.uids()
print p.gids()