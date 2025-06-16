import httpx

from tools.fakers import get_random_email

"""
Авторизация пользователя и получение токена доступа
"""

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login",
                            json=login_payload)  # отправляет POST-запрос с данными в формате JSON на указанный URL и сохраняет ответ в переменную `login_response`.
login_response_data = login_response.json()  # преобразует ответ в формате JSON в словарь Python и сохраняет его в переменную `login_response_data`.
print(f"Данные авторизации: {login_response_data}")  # выводит код состояния ответа и ответ в формате JSON на экран.

accessToken = login_response.json()["token"]["accessToken"]  # извлекает токен доступа из ответа и сохраняет его в переменной `accessToken`.


# создаёт объект `client` класса `httpx.Client`, который будет использоваться для выполнения последовательности запросов
client = httpx.Client(base_url="http://127.0.0.1:8000",
                      headers={"Authorization": f"Bearer {accessToken}"},    # устанавливает заголовок авторизации с токеном доступа.
                      timeout=10)   # устанавливает таймаут в 10 секунд для всех запросов, выполняемых с помощью этого клиента.



get_user_me_response = client.get("/api/v1/users/me") # отправляет GET-запрос на URL `/api/v1/users/me` для получения информации о текущем пользователе и сохраняет ответ в переменную `get_user_me_response`.
get_user_me_response_data = get_user_me_response.json()  # преобразует ответ в формате JSON в словарь Python и сохраняет его в переменную `get_user_me_response_data`.

print(f"Данные пользователя: {get_user_me_response_data}")  # выводит ответ в формате JSON на экран.
