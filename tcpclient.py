#!/usr/bin/env python

import socket

HOST = 'www.google.com'
PORT = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')
    response = client.recv(4096)

print('Received ', repr(response))

