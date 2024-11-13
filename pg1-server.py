# Client Server based Socket Programming

# WAP using Client server socket programming to implement the echo service and date time service.
# Eg: Client: Hello
# Server: Hello

import socket
from datetime import datetime

def start_server(host='localhost', port=3000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on PORT : {port}")

    try:
        conn, addr = server_socket.accept()

        while True:
            data = conn.recv(1024).decode()

            if not data:
                break

            if data.lower() == '#datetime':
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                conn.sendall((str)(current_time).encode())
                print(f"Sent {current_time} to client")
            elif data.lower().startswith('#echo'):
                resp = data[5:]
                conn.sendall(resp.encode())
                print(f"Echoed {resp}")
            else:
                break

    except Exception as e:
        print(f"Error {e} occured")
                
    finally:
        server_socket.close()
        print(f"Connection closed with client {addr}")

start_server()