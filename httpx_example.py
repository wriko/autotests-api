import httpx  # импортирует модуль `httpx`, который используется для работы с HTTP-запросами.

# GET-запрос
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")  # отправляет GET-запрос на указанный URL и сохраняет ответ в переменную `response`.
print(response.status_code)  # выводит код состояния ответа (например, 200 для успешного запроса).
print(response.json())  # выводит содержимое ответа в формате JSON, преобразуя его в словарь Python.

# GET-запрос c параметрами
response = httpx.get("https://jsonplaceholder.typicode.com/todos?userId=1")  # отправляет GET-запрос на указанный URL и сохраняет ответ в переменную `response`.
print(response.url)  # выводит код состояния ответа (например, 200 для успешного запроса).
print(response.json())  # выводит содержимое ответа в формате JSON, преобразуя его в словарь Python.
# или так:
params = {"userId": 1}  # создаёт словарь `params` с параметрами запроса.
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)  # отправляет GET-запрос с параметрами на указанный URL и сохраняет ответ в переменную `response`.
print(response.url)  # выводит код состояния ответа (например, 200 для успешного запроса).
print(response.json())  # выводит содержимое ответа в формате JSON, преобразуя его в словарь Python.


# GET-запрос с передачей заголовков
headers = {"Authorization": "Bearer your_token_here"}  # создаёт словарь `headers` с заголовками, которые будут отправлены в запросе.
response = httpx.get("https://httpbin.org/get", headers=headers)  # отправляет GET-запрос на указанный URL с заголовками и сохраняет ответ в переменную `response`.
print(response.request.headers)  # выводит заголовки запроса, которые были отправлены серверу.)
print(response.json())  # выводит содержимое ответа в формате JSON, преобразуя его в словарь Python.

# POST-запрос JSON
data = {  # создаёт словарь `data` с данными, которые будут отправлены в POST-запросе.
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)  # отправляет POST-запрос с данными в формате JSON на указанный URL и сохраняет ответ в переменную `response`.
print(response.status_code)  # выводит код состояния ответа (например, 200 для успешного запроса).
print(response.json())  # выводит содержимое ответа в формате JSON, преобразуя его в словарь Python.


# POST-запрос с FORMDATA
data = {"username": "test_user", "password": "123456"}  # создаёт словарь `data` с данными для отправки в POST-запросе.
response = httpx.post("https://httpbin.org/post", data=data)  # отправляет POST-запрос с данными в формате FORMDATA на указанный URL и сохраняет ответ в переменную `response`.", json=data)
print(response.status_code)  # выводит код состояния ответа (например, 200 для успешного запроса).
print(response.headers)  # выводит заголовки ответа, которые содержат информацию о типе контента, длине ответа и других метаданных.
print(response.json())  # выводит содержимое ответа в формате JSON, преобразуя его в словарь Python.


# POST-запрос с передачей файла
files = {"file": ("example.txt", open("example.txt", "rb"))} # создаёт словарь `files` с файлом, который будет отправлен в POST-запросе (в данном случае, файл "example.txt"). Ключ "file" указывает на имя параметра формы, а значение является кортежем из имени файла и файла, открытого в бинарном режиме для чтения.
response = httpx.post("https://httpbin.org/post", files=files)  # отправляет POST-запрос с файлом на указанный URL и сохраняет ответ в переменную `response`.
print(response.json())  # выводит содержимое ответа в формате JSON, преобразуя его в словарь Python.


# работа с сессиями

with httpx.Client() as client:  # создаёт объект `client` класса `httpx.Client`, который будет использоваться для выполнения последовательности запросов.
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1") # отправляет GET-запрос на указанный URL с использованием клиента.
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")  # отправляет GET-запрос на указанный URL с использованием клиента.
client.close()  # закрывает клиент после выполнения последовательности запросов

print(response1.json())  # выводит содержимое первого ответа в формате JSON, преобразуя его в словарь Python.
print(response2.json())  # выводит содержимое первого ответа в формате JSON, преобразуя его в словарь Python.

# если нужно в каждом запросе отправлять заголовки, то можно создать клиент с заголовками:
client = httpx.Client(headers={"Authorization": "Bearer your_token_here"})  # создаёт объект `client` класса `httpx.Client` с заголовками, которые будут использоваться для всех запросов, отправляемых через этот клиент.
response = client.get("https://httpbin.org/get") # отправляет GET-запрос на указанный URL с использованием клиента. Заголовки будут включены в запрос.
print(response.json()) # выводит содержимое ответа в формате JSON, преобразуя его в словарь Python.

print("==========================================================================================================================")

# работа с ошибками
try: # пытается выполнить код внутри блока `try`, чтобы обработать возможные ошибки. Если в процессе выполнения возникает исключение, выполнение переходит к блоку `except`. Если исключение не возникает, блок `except` игнорируется.
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")  # отправляет GET-запрос на несуществующий URL, чтобы вызвать ошибку.
    response.raise_for_status()  # вызывает исключение `httpx.HTTPStatusError`, если сервер возвращает код состояния HTTP, указывающий на ошибку (например, 404 или 500). Если код состояния успешный (например, 200), исключение не
except httpx.HTTPStatusError as exc:  # перехватывает исключение `httpx.HTTPStatusError`, которое возникает, если сервер возвращает код состояния HTTP, указывающий на ошибку (например, 404 или 500).
    print(f"Ошибка запроса {exc}, статус код: {exc.response.status_code}")  # выводит сообщение об ошибке и код состояния ответа, который вызвал исключение.

# использование таймаута
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)  # отправляет GET-запрос на указанный URL с таймаутом в 2 секунды. Если сервер не отвечает в течение этого времени, будет вызвано исключение.
except httpx.ReadTimeout as exc: # перехватывает исключение `httpx.ReadTimeout`, которое возникает, если сервер не отвечает в течение указанного времени.
    print("Запрос превысил таймаут:", exc)  # выводит сообщение о превышении таймаута и информацию об исключении.