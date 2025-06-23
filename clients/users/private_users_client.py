from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import GetUserResponseSchema, UpdateUserRequestSchema


class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def get_user_me_api(self) -> Response:
        """
        Метод получения текущего пользователя.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/users/me")


    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получения пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")


    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True)) # Отправляем PATCH-запрос на обновление пользователя с данными из словаря request, преобразованного в JSON с помощью метода model_dump класса UpdateUserRequestShema


    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")


    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Метод получения текущего пользователя.

        :return: Словарь с данными пользователя.
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text) # Преобразуем ответ в словарь с данными пользователя с помощью метода model_validate_json класса GetUserResponseShema


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создает экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))  # Настройка клиента с базовым URL и таймаутом