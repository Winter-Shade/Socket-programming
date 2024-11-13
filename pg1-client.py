# Client Server based Socket Programming

# WAP using Client server socket programming to implement the echo service and date time service.
# Eg: Client: Hello
# Server: Hello

import socket

def start_client(host='localhost', port=3000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))

    try:
        while True:
            service = input('Enter #datetime or #echo or anything else to exit : ')
            client_socket.sendall(service.encode())
            if service.lower()=='#datetime' or (service.lower().startswith('#echo')):
                resp = client_socket.recv(1024).decode()

                print(f"Response received from server :  {resp}")
            else:
                break

    finally:
        client_socket.close()
        print("Connection closed")


start_client()