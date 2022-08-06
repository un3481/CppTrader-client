# -*- coding: utf-8 -*-

import os
import time
import socket

MSG_SIZE = 1024
MSG_SIZE_LARGE = 8192
socket_path = "/home/ubuntu/Documents/GitHub/daemons/testing.sock"

try:
    # Check if file exists
    if not os.path.exists(socket_path):
        raise Exception("socket file doesn't exist")

    # Connect to Socket
    client = socket.socket(
        socket.AF_UNIX,
        socket.SOCK_STREAM
    )
    client.connect(socket_path)

    # Loop Inputs
    while True:
        try:
            x = input("> ") # Input command
            if x != "":
                buffer = bytes(map(ord, x + "\0")) # Create buffer
                buffer += b"\0" * (MSG_SIZE - len(buffer)) # enforce MSG_SIZE
                client.send(buffer) # Send message
                if x == "exit": break
                if x.startswith("get"): # If command recieves response
                    buffer = client.recv(MSG_SIZE_LARGE) # Read MSG_SIZE_LARGE bytes
                    res = ''.join(map(chr, buffer)).split("\0")[0] # Remove extra chars
                    print(res) # Print response
        
        except KeyboardInterrupt:
            print("\n")
            break
        except Exception as e:
            print(f"{e}")
    
    # Close Socket
    client.close()

except Exception as e:
    print(f"{e}")