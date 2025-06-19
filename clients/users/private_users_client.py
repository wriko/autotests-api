from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


# Добавили описание структуры пользователя
class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

# Добавили описание структуры ответа получения пользователя
class GetUserResponseDict(TypedDict):
    """
    Описание структуры ответа получения пользователя.
    """
    user: User


class UpdateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление пользователя.
    """

    email: str | None
    lastName: str | None
    firsName: str | None
    middleName: str | None

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

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")

    # Добавили новый метод
    def get_user(self, user_id: str) -> GetUserResponseDict:
        """
        Метод получения текущего пользователя.

        :return: Словарь с данными пользователя.
        """
        response = self.get_user_api(user_id)
        return response.json()


def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    return PrivateUsersClient(client=get_private_http_client(user))  # Настройка клиента с базовым URL и таймаутом