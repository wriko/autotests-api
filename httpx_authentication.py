import httpx


# Пример использования httpx для аутентификации

login_payload = {
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)  # отправляет POST-запрос с данными в формате JSON на указанный URL и сохраняет ответ в переменную `response`. Данные для запроса берутся из словаря `payload`.
login_response_data = login_response.json()  # преобразует ответ в формате JSON в словарь Python и сохраняет его в переменную `login_response_data`.
print("login_response:", login_response_data)  # выводит ответ в формате JSON на экран.
print("login_response_status_code:", login_response.status_code)  # выводит код состояния ответа на экран.


# Пример использования httpx для аутентификации и обновления токена

refresh_payload = { # создаёт словарь `refresh_payload` с данными для обновления токена.
    "refreshToken": login_response_data["token"]["refreshToken"] # извлекает значение `refreshToken` из ответа на запрос входа в систему и сохраняет его в словаре `refresh_payload`.
}

refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload) # отправляет POST-запрос с данными в формате JSON на указанный URL и сохраняет ответ в переменную `response`. Данные для запроса берутся из словаря `payload`.
refresh_response_data = refresh_response.json() # преобразует ответ в формате JSON в словарь Python и сохраняет его в переменную `refresh_response_data`.

print("refresh_response:", refresh_response_data) # выводит ответ в формате JSON на экран.
print("refresh_response_status_code:", refresh_response.status_code)  # выводит код состояния ответа на экран.