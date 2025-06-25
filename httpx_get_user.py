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
Получение информации о созданном пользователе
"""

client = httpx.Client(base_url="http://localhost:8000/api/v1", headers={"Authorization": f"Bearer {accessToken}"})  # создаёт объект `client` класса `httpx.Client`, который будет использоваться для выполнения последовательности запросов. Устанавливает базовый URL и заголовок авторизации с токеном доступа.

get_user_response = client.get(f"/users/{user_id}") # отправляет GET-запрос на URL `/users/{user_id}` и сохраняет ответ в переменную `get_user_response`.
get_user_response_data = get_user_response.json() # преобразует ответ в формате JSON в словарь Python и сохраняет его в переменную `get_user_response_data`.
print(f"ИНФА О ПОЛЬЗОВАТЕЛЕ:\nСтатус код: {get_user_response.status_code}\nОтвет: {get_user_response_data}") # выводит код состояния ответа и ответ в формате JSON на экран.