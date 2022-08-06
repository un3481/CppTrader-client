# -*- coding: utf-8 -*-

import os
import socket

MSG_SIZE = 1024
MSG_SIZE_LARGE = 8192
socket_path = "/home/ubuntu/Documents/GitHub/daemons/testing.sock"

try:
    
    if not os.path.exists(socket_path):
        raise Exception("socket file doesn't exist")

    client = socket.socket(
        socket.AF_UNIX,
        socket.SOCK_STREAM
    )
    client.connect(socket_path)

    while True:
        try:
            x = input("> ")
            if x != "":
                client.send(
                    bytes(map(ord, x + "\n"))
                )
                if x == "exit": break
                if x.startswith("get"):
                    res = client.recv(MSG_SIZE_LARGE)
                    print(
                        ''.join(map(chr, res))
                    )
        
        except KeyboardInterrupt: break
        except Exception as e: print(f"{e}")
    
    client.close()

except Exception as e: print(f"{e}")