#!/usr/bin/env python

import socket

SERVER = '0.0.0.0'
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER, PORT))

client.sendall(bytes('This is from client', 'UTF-8'))

while True:
    response = client.recv(4096)
    print('From Server: ', response.decode())
    req = input()
    client.sendall(bytes(req, 'UTF-8'))
    if req == 'bye':
        break
