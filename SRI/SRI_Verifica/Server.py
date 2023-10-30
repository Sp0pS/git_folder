import socket
import threading

HOST = socket. gethostbyname(socket.gethostname())
PORT = 5055

def remooveVowels(str):
    vowels = 'aeiouAEIOUàèìòù'
    new_str = ''
    for char in str:
        if not vowels.__contains__(char):
            new_str = new_str+char
    return new_str

def alfabetoFarfallino(message):
    VOWELS = 'aeiouAEIOUàèìòù'
    new_str = ""
    for char in message:
        if VOWELS.__contains__(char):
            new_str = new_str + char + "f" +char
        else:
            new_str = new_str + char
    return new_str



def serverScript(client_connection):
    with client_connection:
        client_connection.send("saluta(ciao)!! ".encode())
        saluto = client_connection.recv(1024).decode()
        print(saluto)
        if saluto == "ciao":
            client_connection.send("modalità 1 : togli le vocale\nmodalità 2 : to upper\nmodalità 3 : conta parole\nmodalità 4 : conta caratteri\nmodalità 5 : stampa bravo\nmodalita 6 : alfabeto farfallino\n\nscegli la modalità: ".encode())
            mod = client_connection.recv(1024).decode()
            client_connection.send("inserisci la stringa: ".encode())
            message = client_connection.recv(1024).decode()

            match mod:
                case "1":
                    client_connection.send(("risultato: "+ remooveVowels(message)).encode())
                case "2":
                    client_connection.send(("risultato: "+ message.upper()).encode())
                case "3":
                    client_connection.send(("risultato: "+ len(str.split())).encode())
                case "4":
                    client_connection.send(("risultato: "+ len(message)).encode())
                case"5":
                    client_connection.send("bravo".encode())
                case "6":
                    client_connection.send(("risultato: " + alfabetoFarfallino(message)).encode())
                case _:
                    client_connection.send("nessuna opzione selezionata".encode())
        else:
            client_connection.send("intanto si saluta".encode())



def startServer():
    with socket.socket() as sock:
        sock.bind((HOST,PORT))
        sock.listen()
        client_connection, client_address =sock.accept()
        print("new connection")
        t1 = threading.Thread(target=serverScript, args=(client_connection,))
        t1.start()
        t1.join()

if __name__ == "__main__":
    startServer()

