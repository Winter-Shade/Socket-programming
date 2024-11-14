import socket

def start_client(host='localhost', port=3000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Type quit to end the chat")

    while True:
        msg = input('You : ')
        client_socket.sendto(msg.encode(), (host, port))

        if msg.lower() == 'quit':
            break

        reply, _ = client_socket.recvfrom(1024)
        print(f"Server: {reply.decode()}")

    client_socket.close()

start_client()