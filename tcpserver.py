import socket, threading

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientSocket):
        threading.Thread.__init__(self)
        self.caddress = clientAddress
        self.csocket = clientSocket
        print('New connection added: ', clientAddress)
    def run(self):
        print('Connection from: ', self.caddress)
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()

            if msg == 'bye':
                break
            print('From client: ', msg)
            self.csocket.send(bytes(msg, 'utf-8'))
        print('Client at ', self.caddress, 'disconnected...')

BIND_IP  = '0.0.0.0'
BIND_PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((BIND_IP, BIND_PORT))

print('[*] Listening on %s:%d' %(BIND_IP, BIND_PORT))
print('Waiting for client request...')

while True:
    server.listen(1)
    clientsocket, clientaddress = server.accept()

    print('[*] Accepted connection from: %s:%d' %(clientaddress[0], clientaddress[1]))

    thread = ClientThread(clientaddress, clientsocket)
    thread.start()
