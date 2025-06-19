from clients.api_client import APIClient   #  импортируем базовый класс ApiClient для выполнения HTTP-запросов
from httpx import Response  # импортируем класс Response из библиотеки httpx для работы с ответами на HTTP-запросы
from typing import TypedDict # импортируем TypedDict для создания словарей с фиксированными ключами и типами значений

from clients.public_http_builder import get_public_http_client

class Token(TypedDict): # создаем словарь с фиксированными ключами и типами значений для токена авторизации
    """
    Описание структуры токена авторизации.
    """
    tokenType: str # ключ tokenType должен быть строкой
    accessToken: str # ключ accessToken должен быть строкой
    refreshToken: str # ключ refreshToken должен быть строкой


class LoginRequestDict(TypedDict): # создаем словарь с фиксированными ключами и типами значений для запроса авторизации
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str # ключ email должен быть строкой
    password: str # ключ password должен быть строкой


class LoginResponseDict(TypedDict):
    """
    Описание структуры ответа на запрос авторизации.
    """
    token: Token # ключ token должен быть словарем с фиксированными ключами и типами значений, описанными в классе Token


class RefreshRequestDict(TypedDict): # создаем словарь с фиксированными ключами и типами значений для запроса обновления токена
    """
    Описание структуры запроса для обновления токена.
    """
    refreshToken: str # ключ refreshToken должен быть строкой



class AuthenticationClient(APIClient): # создаем класс AuthenticationClient, который наследуется от ApiClient для выполнения запросов к API авторизации
    """
    Клиент для работы с /api/v1/authentication
    """

    def login_api(self, request: LoginRequestDict) -> Response: # создаем метод для отправки запроса на авторизацию
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/authentication/login', json = request) # отправляем POST-запрос на эндпоинт /api/v1/authentication/login с данными запроса в формате JSON


    def refresh_api(self, request: RefreshRequestDict) -> Response: # создаем метод для отправки запроса на обновление токена
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/authentication/refresh', json = request)


    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        """
        Метод выполняет аутентификацию пользователя и возвращает токен авторизации.
        """
        response = self.login_api(request) # вызываем метод для отправки запросана авторизацию и получаем ответ
        return response.json() # # возвращаем токен авторизации из ответа сервера в формате JSON


# Добавляем builder для AuthenticationClient
def get_authentication_client() -> AuthenticationClient:
    """
    Функция создает экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: AuthenticationClient.
    """
    return AuthenticationClient(client = get_public_http_client())  # Настройка клиента с базовым URL и таймаутом
