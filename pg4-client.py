import socket

def start_client(host='localhost', port=3000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))

        while True:
            msg = input('Enter message or quit: ')
            client_socket.sendall(msg.encode())
            if msg.lower() == 'quit':
                break

            msg = client_socket.recv(1024).decode()
            if msg.lower() == 'quit':
                break
            print(f"Server: {msg}")

    except Exception as e:
        print(f"Error {e} has occured")

    finally:
        client_socket.close()
        print("Connection closed")

start_client()