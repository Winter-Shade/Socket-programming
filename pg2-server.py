# WAP using Client server socket programming to check if the given string is palindrome

import socket

def palindrome(s):
    n = len(s)
    i, j = 0, n-1
    while i<j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def start_server(host='localhost', port=3000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening for connections on PORT {port}")

    try:
        conn, addr = server_socket.accept()

        data = conn.recv(1024).decode()
        print(f"Received {data} from client")
        isPalindrome = palindrome(data)
        conn.sendall((str)(isPalindrome).encode())
        print(f"Sent {isPalindrome} to client")

    except Exception as e:
        print(f"Error {e} has occured")

    finally:
        server_socket.close()
        print("Server socket closed")


start_server()