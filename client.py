# -*- coding: utf-8 -*-

import os
import socket

MSG_SIZE = 1024
MSG_SIZE_LARGE = 8192
socket_path = "/home/ubuntu/GitHub/daemons/testing.sock"

try:
    
    if os.path.exists(socket_path):
        raise "no file"

    client = socket.socket(
        socket.AF_UNIX,
        socket.SOCK_STREAM
    )
    client.connect(socket_path)

    while True:
        try:
            x = input("> ")
            if x != "":
                client.send(x + "\n")
                if x == "exit": break
                if x.startswith("get"):
                    res = client.recv(MSG_SIZE_LARGE)
                    print(res)
        except KeyboardInterrupt: break

    client.close()

except: print("Couldn't Connect!")