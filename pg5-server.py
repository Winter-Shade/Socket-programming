# Write a socket program to implement the UDP based chat application between client and server.

import socket
import os

def start_server(host='localhost', port=3000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_socket.bind((host, port))
    print(f"Server Started ; Listening for connections on PORT:{port}")

    while True:
        msg, clientAddr = server_socket.recvfrom(1024)
        msg = msg.decode()
        if msg.lower() == 'quit':
            break
        print(f"Msg. received: {msg}")

        msg = input('Type your msg: ')
        server_socket.sendto(msg.encode(), clientAddr)

    server_socket.close()


start_server()