# -*- coding: utf-8 -*-

import os
import time
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
                buffer = bytes(map(ord, x + "\0"))
                buffer += b"\0" * (MSG_SIZE - len(buffer))
                client.send(buffer)
                if x == "exit": break
                if x.startswith("get"):
                    buffer = client.recv(MSG_SIZE_LARGE)
                    res = ''.join(map(chr, buffer)).split("\0")[0]
                    print(res)
        
        except KeyboardInterrupt:
            print("\n")
            break
        except Exception as e:
            print(f"{e}")
    
    client.close()

except Exception as e:
    print(f"{e}")