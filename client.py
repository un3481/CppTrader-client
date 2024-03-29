# -*- coding: utf-8 -*-

import os
import sys
import socket

MSG_SIZE = 1024
MSG_SIZE_LARGE = 8192

try:
    # Check input path
    if len(sys.argv) < 2:
        raise Exception("no path provided to socket file")
    
    # Get input path
    socket_path = sys.argv[1]
    
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
            cmd = input("> ") # Input command
            buffer = bytes(map(ord, cmd + "\0")) # Create buffer
            buffer += b"\0" * (MSG_SIZE - len(buffer)) # enforce MSG_SIZE
            client.send(buffer) # Send message
            if cmd == "exit": break
            if cmd.startswith("get"): # If command recieves response
                buffer = client.recv(MSG_SIZE_LARGE) # Read MSG_SIZE_LARGE bytes
                res = ''.join(map(chr, buffer)).split("\0")[0] # Remove extra chars
                print(res) # Print response
        
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"{e}")
    
    # Close Socket
    client.close()

except Exception as e:
    print(f"{e}")