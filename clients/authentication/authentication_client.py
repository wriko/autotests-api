from clients.api_client import ApiClient   #  импортируем базовый класс ApiClient для выполнения HTTP-запросов
from httpx import Response  # импортируем класс Response из библиотеки httpx для работы с ответами на HTTP-запросы
from typing import TypedDict # импортируем TypedDict для создания словарей с фиксированными ключами и типами значений


class LoginRequestDict(TypedDict): # создаем словарь с фиксированными ключами и типами значений для запроса авторизации
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str # ключ email должен быть строкой
    password: str # ключ password должен быть строкой


class RefreshRequestDict(TypedDict): # создаем словарь с фиксированными ключами и типами значений для запроса обновления токена
    """
    Описание структуры запроса для обновления токена.
    """
    refreshToken: str # ключ refreshToken должен быть строкой



class AuthenticationClient(ApiClient): # создаем класс AuthenticationClient, который наследуется от ApiClient для выполнения запросов к API авторизации
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
