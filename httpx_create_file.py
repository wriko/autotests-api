import httpx
from tools.fakers import fake

"""
Создание пользователя
"""

create_user_payload = {
  "email": fake.email(), # использует функцию `get_random_email` для генерации случайного адреса электронной почты.
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)  # отправляет POST-запрос с данными в формате JSON на указанный URL и сохраняет ответ в перем енную `response`.
create_user_response_data = create_user_response.json()  # преобразует ответ в формате JSON в словарь Python и сохраняет его в переменную `create_user_response_data`.
print(f"Create user data: {create_user_response_data}")  # выводит ответ в формате JSON на экран.


user_id = create_user_response_data["user"]["id"] # извлекает идентификатор пользователя из ответа и сохраняет его в переменной `user_id`.


"""
Авторизация пользователя и получение токена доступа
"""

login_payload = {        # создаёт словарь `login_payload` с данными для входа в систему.
  "email": create_user_payload["email"], # использует адрес электронной почты, который был сгенерирован при создании пользователя.
  "password": create_user_payload["password"] # использует пароль, который был указан при создании пользователя.
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload) # отправляет POST-запрос с данными в формате JSON на указанный URL и сохраняет ответ в переменную `login_response`.
login_response_data = login_response.json() # преобразует ответ в формате JSON в словарь Python и сохраняет его в переменную `login_response_data`.
print(f"Данные авторизации: {login_response_data}") # выводит код состояния ответа и ответ в формате JSON на экран.

accessToken = login_response.json()["token"]["accessToken"] # извлекает токен доступа из ответа и сохраняет его в переменной `accessToken`.

"""
Загрузка файла
"""

create_file_headers = {  # создаёт словарь `create_file_header`, который будет использоваться в заголовках запроса для загрузки файла.
    "Authorization": f"Bearer {accessToken}", # добавляет заголовок `Authorization` с токеном доступа к заголовкам запроса.
}

create_file_response = httpx.post(  # создаёт переменную `create_file_response`, которая будет использоваться для отправки запроса на загрузку файла.
    "http://localhost:8000/api/v1/files", # отправляет POST-запрос на указанный URL для загрузки файла.
    data={"filename": "image.png", "directory": "courses"}, # отправляет POST-запрос на указанный URL с данными в формате JSON и сохраняет ответ в переменную  `create_file_response`. `filename` и `directory` - ключи в словаре данных, которые содержат название файла и путь к каталогу, в который нужно загрузить файл соответственно.
    files={"upload_file": open("./testdata/files/image.png", "rb")}, # отправляет файл `image.png` из локальной файловой системы в формате двоичных данных (binary) с помощью ключа `upload_file`.
    headers=create_file_headers # добавляет заголовки запроса, которые были созданы ранее.
)
create_file_response_data = create_file_response.json()
print(f"Create file data: {create_file_response_data}")  # выводит ответ в формате JSON на экран.
