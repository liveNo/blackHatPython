# coding=utf-8
#/usr/bin/python

import sys
import socket
import getopt
import threading
import subprocess

# 定义一些全局变量
listen = False
command = False
upload = False
execure = ""
target = ""
upload_destination = ""
port = 0




# 1
def usage ():
    print "BHP Net Tool"
    print
    print "Usage: bhpnet.py -t target_host -p port"
    print "-l --listen               - listen on [host]:[port] for incoming connections"
    print "-e --execute=file_to_run - execute the given file upon receiving a connection"
    print "-c --command - initialize a command shell"
    print "-u --upload=destination - upon receiving connection upload a file and write to [destination]"
    print
    print
    print "Example:"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -u=/var/www/a.py"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
    print "echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135"
    sys.exit(0)


def main ():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    # 读取命令行选项
    try:
        opts, args = getopt.getopt(sys.argv[1:], "Hle:t:p:cu:", ["help", "listen", "execute", "target", "port", "command", "upload"])

    except getopt.GetoptError as err:
        print str(err)
        usage()

    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False, "Unhandled Option"




    if not listen and len(target) and port > 0:
        #
        #
        buffer = sys.stdin.read()

        # 发送数据
        client_sender(buffer)

    # 我们开始监听并准备上传文件，执行命令
    # 放置一个反弹Shell
    # 取决于上面命令选项
    if listen:
        server_loop();



main()