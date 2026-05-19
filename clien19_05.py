import asyncio
import websockets
import socket


server_address = ('localhost', 8765)
with socket.create_connection(server_address) as sock:
    amount_received = 0
    amount_expected = 12
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        mess = data.decode()
        print(f'вооооу : {data.decode()}')

print('отключаемся ', server_address )

