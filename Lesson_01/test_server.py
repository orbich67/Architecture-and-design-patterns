import socket

transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 8001)
transport.bind(server_address)
transport.listen(1)

while True:
    print('Waiting connection...')
    client, client_address = transport.accept()
    print(f'Connection request from: {client_address}')
    data = client.recv(1024).decode('utf-8')
    print(data)
    client.close()
