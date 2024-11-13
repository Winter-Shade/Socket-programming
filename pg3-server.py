# Using TCP/IP sockets, write a client-server program to make the client send the file name and to make the server send back the contents of the requested file if present.

import socket
import os

def start_server(host='localhost', port=3000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Listening for connections on PORT:{port}")

    try:
        conn, addr = server_socket.accept()

        filename = conn.recv(1024).decode()
        
        if os.path.isfile(filename):
            file = open(filename, 'r')
            contents = file.read()
            conn.sendall(contents.encode())
            print("Sent contents of file to server")
        else:
            err = "Sorry file does not exist"
            print(err)
            conn.sendall(err.encode())

    except Exception as e:
        print(f"Error {e} has occured")

    finally:
        server_socket.close()
        print("Connection Closed")

start_server()