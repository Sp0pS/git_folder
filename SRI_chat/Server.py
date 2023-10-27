import socket
import threading

HOST = '192.168.55.58'
PORT = 5055
clients = []





def host_handler(socket_connection, addr):
    with socket_connection:
        while True:
            data = socket_connection.recv(1024)
            if not data:
                break

            print( addr, " send ",data)
            for client in clients:
                if client != socket_connection:
                    client.send(data)



with socket.socket() as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        socket_connection, address = s.accept()
        print("new connection")
        clients.append(socket_connection)
        t1 = threading.Thread(target=host_handler, args=(socket_connection, address,))
        t1.start()



