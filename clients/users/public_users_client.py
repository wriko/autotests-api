from clients.api_client import ApiClient  # импортируем базовый класс ApiClient для выполнения HTTP-запросов
from httpx import Response  # импортируем класс Response из библиотеки httpx для работы с ответами на HTTP-запросы
from typing import TypedDict  # импортируем TypedDict для создания словарей с фиксированными ключами и типами значений


class CreateUserRequestDict(TypedDict):  # создаем класс CreateUserDict, который наследуется от TypedDict для создания словарей с фиксированными ключами и типами значений
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(
    ApiClient):  # создаем класс PublicUsersClient, который наследуется от ApiClient для выполнения запросов к API создания пользователя
    """
    Клиент для работы с /api/v1/users для создания пользователя
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:  # создаем метод для отправки запроса на создание пользователя в системе и получение ответа от сервера
        """
        Метод выполняет создание нового пользователя в системе с помощью POST-запроса.

        :param request: Словарь с данными запроса, содержащим следующие поля: email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/users',json=request)  # отправляем POST-запрос на эндпоинт /api/v1/users с данными запроса в формате JSON
