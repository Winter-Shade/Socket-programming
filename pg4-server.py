# Write a socket program to implement the TCP based chat application between client and server.

import socket
import os

def start_server(host='localhost', port=3000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Listening for connections on PORT:{port}")

    try:
        conn, addr = server_socket.accept()

        while True:
            msg = conn.recv(1024).decode()
            if msg.lower() == 'quit':
                break
            print(f"Client {addr} : {msg}")

            msg = input('Enter message or quit: ')
            conn.sendall(msg.encode())
            if msg.lower() == 'quit':
                break
        
    except Exception as e:
        print(f"Error {e} has occured")

    finally:
        server_socket.close()
        print("Connection Closed")

start_server()