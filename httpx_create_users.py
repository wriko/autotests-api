import httpx
from tools.fakers import fake

payload = {
  "email": fake.email(), # использует функцию `get_random_email` для генерации случайного адреса электронной почты.
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

response = httpx.post("http://localhost:8000/api/v1/users", json=payload)  # отправляет POST-запрос с данными в формате JSON на указанный URL и сохраняет ответ в перем енную `response`.

print(response.status_code)
print(response.json())