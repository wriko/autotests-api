from clients.api_client import APIClient  # импортируем базовый класс ApiClient для выполнения HTTP-запросов
from httpx import Response  # импортируем класс Response из библиотеки httpx для работы с ответами на HTTP-запросы
from typing import TypedDict  # импортируем TypedDict для создания словарей с фиксированными ключами и типами значений
from clients.public_http_builder import get_public_http_client


class User(TypedDict):  # создаем класс User, который наследуется от TypedDict для создания словарей с фиксированными ключами и типами значений
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserRequestDict(TypedDict):  # создаем класс CreateUserDict, который наследуется от TypedDict для создания словарей с фиксированными ключами и типами значений
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


# Добавили описание структуры ответа создания пользователя
class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: User


class PublicUsersClient(APIClient):  # создаем класс PublicUsersClient, который наследуется от ApiClient для выполнения запросов к API создания пользователя
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

    # Добавили новый метод
    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict: # создаем метод для отправки запроса на создание пользователя в системе и получения ответа от сервера и преобразования ответа в словарь с данными пользователя
        response = self.create_user_api(request)  # вызываем метод create_user_api для отправки запроса на создание пользователя и получения ответа от сервера
        return response.json() # преобразуем ответ в JSON для удобства чтения и проверки его содержимого


# Добавляем builder для PublicUsersClient
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создает экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client = get_public_http_client())
