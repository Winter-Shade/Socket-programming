# Using TCP/IP sockets, write a client-server program to make the client send the file name and to make the server send back the contents of the requested file if present.

import socket

def start_client(host='localhost', port=3000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))

        filename = input('Enter filename to get contents : ')
        client_socket.sendall(filename.encode())

        response = client_socket.recv(4096).decode()
        print(f"Response from server : \n{response}")

    except Exception as e:
        print(f"Error {e} has occured")

    finally:
        client_socket.close()
        print("Connection closed")

start_client()