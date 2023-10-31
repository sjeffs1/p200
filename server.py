import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = "127.0.0.1"
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []
nicknames = []
print("server is running...")

def clientThread(connection, address):
    connection.send("welcome to this chatroom!". encode("utf-8"))
    while True:
        try:
            message = connection.recv(2048).decode("utf-8")
            if message:
                print(message)
                broadcast(message, connection)
            else:
                remove(connection)
                removenickname(nickname)
        except:
            continue

def broadcast(message, connection):
    for client in list_of_clients:
        if client!=connection:
            try:
                client.send(message.encode("utf-8"))
            except:
                remove(client)

def remove(connection):
    for connection in list_of_clients:
        list_of_clients.remove(connection)

def removenickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)

while True:
    connection, address = server.accept()
    connection.send("NICKNAME".encode("utf-8"))
    nickname = connection.recv(2048).decode("utf-8")

    list_of_clients.append(connection)
    nicknames.append(nickname)

    message = "{} join".format(nickname)

    print(message)

    broadcast(message, connection)

    new_thread = Thread(target = clientThread, args=(connection, nickname))
    new_thread.start()