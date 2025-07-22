from httpx import Client
from pydantic import BaseModel
from functools import lru_cache
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.event_hooks import curl_event_hook
from config import settings


class AuthenticationUserSchema(BaseModel, frozen=True): # Используем frozen=True для создания неизменяемого объекта, что позволяет использовать его в качестве ключа кэша
    email: str
    password: str

@lru_cache(maxsize=None) # Кэширование для оптимизации повторного использования клиента для аутентификации и доступа к приватным API
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создает экземпляр httpx.Client с аутентификацией пользователя.

    :param user: объект AuthenticationUserSchema, содержащий email и password пользователя
    :return: экземпляр httpx.Client с установленным заголовком Authorization
    """
    autentication_client = get_authentication_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = autentication_client.login(login_request)

    return Client(base_url=settings.http_client.client_url,
                  timeout=settings.http_client.timeout,
                  headers={"Authorization": f"Bearer {login_response.token.access_token}"},
                  event_hooks={"request": [curl_event_hook]}  # Добавляем хук для логирования
                  )