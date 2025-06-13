import socket # импортирует модуль `socket`, который предоставляет функции для работы с сетью.


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создает сокет TCP

server_address = ('localhost', 12345) # задает адрес сервера
client_socket.connect(server_address) # подключается к серверу

message = "Привет, сервер!" # задает сообщение
client_socket.send(message.encode()) # отправляет сообщение серверу

response = client_socket.recv(1024).decode() # получает ответ от сервера и декодирует его в строку utf-8.
print(response) # выводит ответ на экран

client_socket.close() # закрывает сокет