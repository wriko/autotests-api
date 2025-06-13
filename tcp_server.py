import socket # импортирует модуль `socket`, который предоставляет функции для работы с сетью.


def tcp_server(): # определяет функцию `tcp_server`, которая создает TCP-серве
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создает объект `server_socket`, который используется для работы с TCP-соединениями

    server_address = ('localhost', 12345) # задает адрес сервера
    server_socket.bind(server_address) # связывает сокет с адресом сервера

    server_socket.listen(5) # начинает прослушивание входящих соединений на сервере. Параметр `5` указывает максимальное количество соединений в очереди.
    print('Waiting for connection...') # выводит сообщение о том, что сервер ожидает подключения


    while True: # бесконечный цикл, который будет выполняться, пока сервер работает
        client_socket, client_address = server_socket.accept() # принимает входящее соединение и возвращает объект `client_socket`, который используется для работы с клиентским соединением, и адрес клиента.
        print(f"Подключение от {client_address}")

        data = client_socket.recv(1024).decode() # получает данные от клиента и декодирует их в строку
        print(f"Получено сообщение: {data}")

        response = f"Сервер получил сообщение, {data}!"
        client_socket.send(response.encode()) # отправляет ответ клиенту и кодирует его в байты

        client_socket.close() # закрывает сокет клиента


if __name__ == '__main__': # проверяет, запущен ли скрипт напрямую или импортирован в другой скрипт.
    tcp_server() # вызывает функцию `tcp_server`, которая запускает TCP-сервер.