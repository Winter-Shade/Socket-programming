import socket

def start_client(host='localhost', port=3000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))

    except Exception as e:
        print(f"Error {e} has occured")

    finally:
        client_socket.close()
        print("Connection closed")

start_client()