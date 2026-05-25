import socket

h = 'localhost'
p = 8765

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((h, p))
server.listen()

print("сервер запущен и ждёт подключение...")

client_socket, client_address = server.accept()

print(f"подключился клиент: {client_address}")

while True:
    message = client_socket.recv(1024).decode()

    if not message:
        break

    print(f"клиент написал : {message}")

    answer = input("введите сообщение клиенту - ")

    client_socket.send(answer.encode())

client_socket.close()
server.close()







import socket

h = 'localhost'
p = 8765

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((h, p))

print("подключено к серверу!")

while True:
    message = input("вы - ")

    client.send(message.encode())

    data = client.recv(1024).decode()

    print(f"сервер: {data}")
