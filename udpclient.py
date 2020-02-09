#!/usr/bin/env python

import socket

HOST = '127.0.0.1'
PORT = 80

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.sendto(b'Black gold is loading...', (HOST, PORT))
    response, addr = client.recvfrom(4096)

print('Received ', repr(response))

