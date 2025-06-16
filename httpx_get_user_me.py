import httpx             # импортирует модуль `httpx`, который используется для работы с HTTP-запросами.


login_payload = {        # создаёт словарь `login_payload` с данными для входа в систему.
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload) # отправляет POST-запрос с данными в формате JSON на указанный URL и сохраняет ответ в переменную `login_response`.
login_response_data = login_response.json() # преобразует ответ в формате JSON в словарь Python и сохраняет его в переменную `login_response_data`.
print(login_response.status_code) # выводит код состояния ответа (например, 200 для успешного запроса).
print(login_response_data) # выводит ответ в формате JSON на экран.

accessToken = login_response.json()["token"]["accessToken"] # извлекает токен доступа из ответа и сохраняет его в переменной `accessToken`.

client = httpx.Client(base_url="http://localhost:8000/api/v1", headers={"Authorization": f"Bearer {accessToken}"})  # создаёт объект `client` класса `httpx.Client`, который будет использоваться для выполнения последовательности запросов. Устанавливает базовый URL и заголовок авторизации с токеном доступа.

users_me_response = client.get("/users/me") # отправляет GET-запрос на указанный URL с использованием клиента и сохраняет ответ в переменную `users_me_response`.
users_me_response_data = users_me_response.json() # преобразует ответ в формате JSON в словарь Python и сохраняет его в переменную `users_me_response_data`.
print(users_me_response.status_code)     # выводит код состояния ответа (например, 200 для успешного запроса).
print(users_me_response_data)   # выводит ответ в формате JSON на экран.

