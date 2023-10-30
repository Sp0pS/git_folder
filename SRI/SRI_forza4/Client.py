import socket
import threading

HOST = socket. gethostbyname(socket.gethostname())
PORT = 5055

def clientFunction(socket_client):
    with socket_client as sc:
        while True:
            server_message = sc.recv(2048).decode()
            client_message = input(server_message)
            client_message = bytes(client_message, 'utf-8')
            sc.sendall(client_message)


def connectToServer():
    with socket.socket() as socket_client:
        socket_client.connect((HOST, PORT))
        t1 = threading.Thread(target=clientFunction, args=(socket_client,))
        t1.start()
        t1.join()

if __name__ == '__main__':
    connectToServer()
