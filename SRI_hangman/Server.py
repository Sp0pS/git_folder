import random
import socket
from threading import Thread

HOST = socket. gethostbyname(socket.gethostname())
PORT = 5055

WORLDS = ["ciao", "come", "va"]


def game():
    random.shuffle(WORLDS)
    random_world = WORLDS.pop()

    guessed_world = "_" * len(random_world)

    for i in range(4):
        #recived_world = client_connection.recv().decode()
        recived_world = input("world: "+ guessed_world + "   ->input a world or a letter: ")


        if random_world.__contains__(recived_world):
            if random_world == recived_world:
                print("game over: you won!!")
                return 1

            temp = list(guessed_world)
            for j in range(len(recived_world)):
                temp[random_world.index(recived_world) + j] = recived_world[j]
            guessed_world  = "".join(temp)


            if random_world == guessed_world:
                print("game over: you won!!")
                return 1

            print("correct", 4-(i+1),"lives left\n")
        else:
            print("wrong", 4-(i+1),"lives left\n")



        if random_world == guessed_world:
            print("game over: you won!!")



    print("game over: you lost!!")
    return 0



def startServer():
    with socket.socket() as sock:
        sock.bind(HOST, PORT)
        sock.listen()
        client_connection, client_address =sock.accept()


if __name__ == "__main__":
    #startServer()
    game()

