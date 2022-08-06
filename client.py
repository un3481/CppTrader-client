# -*- coding: utf-8 -*-

from msilib.schema import Error
import os
import socket

MSG_SIZE = 1024
MSG_SIZE_LARGE = 8192
socket_path = "/home/ubuntu/Documents/GitHub/daemons/testing.sock"

try:
    
    if os.path.exists(socket_path):
        raise Exception("no file")

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

except Exception as e:
    print(f"Couldn't Connect! : {e}")