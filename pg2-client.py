# Client server socket programming to check if the given string is palindrome

import socket

def start_client(host='localhost', port=3000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))

        str = input('Enter string to send to server : ')

        client_socket.sendall(str.encode())

        data = client_socket.recv(1024).decode()

        if data=='True':
            print('String is palindrome')
        else:
            print('Not palindrome')

    except Exception as e:
        print(f"Error {e} has occured")

    finally:
        client_socket.close()
        print("Connection ended")

start_client()