import socket
import threading

BIND_IP = '0.0.0.0'
BIND_PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((BIND_IP, BIND_PORT))
    server.listen(5)

    print('[*] Listening on %s:%d' %(BIND_IP, BIND_PORT))

    def handle_client(client_socket):
        data = client_socket.recv(1024)

        print('[*] Received: %s' %data)

        client_socket.send(b'ACK!')
        client_socket.close()

    while True:
        client, addr = server.accept()

        with client:
            print('[*] Accepted connection from: %s:%d' %(addr[0], addr[1]))

            client_handler = threading.Thread(target = handle_client, args = (client, ))
            client_handler.start()
