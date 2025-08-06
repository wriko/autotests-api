from httpx import Response  # импортируем класс Response из библиотеки httpx для работы с ответами на HTTP-запросы

from clients.api_coverage import tracker
from clients.public_http_builder import get_public_http_client # импортируем функцию get_public_http_client для создания HTTP-клиента с настройками для публичных запросов
from clients.api_client import APIClient  # импортируем базовый класс ApiClient для выполнения HTTP-запросов
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema # импортируем схемы CreateUserRequestSchema и CreateUserResponseSchema для создания и получения данных пользователя
import allure

from tools.routes import APIRoutes



class PublicUsersClient(APIClient):  # создаем класс PublicUsersClient, который наследуется от ApiClient для выполнения запросов к API создания пользователя
    """
    Клиент для работы с /api/v1/users для создания пользователя
    """

    @allure.step("Создание пользователя")
    @tracker.track_coverage_httpx(APIRoutes.USERS)
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:  # создаем метод для отправки запроса на создание пользователя в системе и получение ответа от сервера
        """
        Метод выполняет создание нового пользователя в системе с помощью POST-запроса.

        :param request: Словарь с данными запроса, содержащим следующие поля: email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(APIRoutes.USERS,json=request.model_dump(by_alias=True))  # отправляем POST-запрос на создание пользователя с данными из словаря request, преобразованного в JSON с помощью метода model_dump класса CreateUserRequestSchema


    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema: # создаем метод для отправки запроса на создание пользователя в системе и получения ответа от сервера и преобразования ответа в словарь с данными пользователя
        response = self.create_user_api(request)  # вызываем метод create_user_api для отправки запроса на создание пользователя и получения ответа от сервера
        return CreateUserResponseSchema.model_validate_json(response.text) # преобразуем ответ в словарь с данными пользователя с помощью метода model_value_json класса CreateUserResponseShema


# Добавляем builder для PublicUsersClient
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создает экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client = get_public_http_client())
