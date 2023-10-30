import socket
import threading

HOST = socket. gethostbyname(socket.gethostname())
PORT = 5055

def remooveVowels(str):
    vowels = 'aeiou'
    new_str = ''
    for char in str:
        if not vowels.__contains__(char):
            new_str = new_str+char
    return new_str


def serverScript(client_connection):
    with client_connection:
        message = client_connection.recv().decode()
        saluto = input("saluta(ciao)!! ")
        if saluto == "ciao":
            mod = input("modalità 1 : togli le vocale\nmodalità 2 : to upper\nmodalità 3 : conta parole\nmodalità 4 : conta caratteri\nmodlità 5 : stampa bravo\n\nscegli la modalità: ")
            message = input("inserisci la stringa: ")

            match mod:
                case "1":
                    client_connection.send(("risultato: ", remooveVowels(message)).encode())
                    print("risultato: ", remooveVowels(message))
                case "2":
                    client_connection.send(("risultato: ", message.upper()).encode())
                    print("risultato: ", message.upper())
                case "3":
                    client_connection.send(("risultato: ", len(str.split())).encode())
                    print("risultato: ", len(str.split()))
                case "4":
                    client_connection.send(("risultato: ", len(message)).encode())
                    print("risultato: ", len(message))
                case"5":
                    client_connection.send("bravo".encode())
                    print("bravo")
                case _:
                    client_connection.send("nessuna opzione selezionata".encode())
                    print("nessuna opzione selezionata")
        else:
            client_connection.send("intanto si saluta".encode())

def startServer():
    with socket.socket() as sock:
        sock.bind(HOST,PORT)
        sock.listen()
        client_connection, client_address =sock.accept()
        t1 = threading.Thread(target=startServer, args=(client_connection,))
        t1.join()

if __name__ == "__main__":
    startServer()

