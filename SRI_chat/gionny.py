import threading
import socket

def print_message(connection):
    while True:
        data = connection.recv(1024)
        if data:
            print("-", data.decode())
        else:
            print("nessun messaggio")

def send_message(connection):
    while True:

        message = input(">")
        message = bytes(message, 'utf-8')

        connection.send(message)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_client:
    socket_client.connect(('192.168.55.209', 5005))
    t1 = threading.Thread(target=send_message, args=(socket_client,))
    t2 = threading.Thread(target=print_message, args=(socket_client,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


                                                                                                         