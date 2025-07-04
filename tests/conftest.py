import pytest
from pydantic import BaseModel, EmailStr

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
# Импортируем API клиенты
from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient



# Модель для агрегации возвращаемых данных фикстурой function_user
class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr: # Быстрый доступ к email пользователя
        return self.request.email

    @property
    def password(self) -> str: # Быстрый доступ к password пользователя
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema (email=self.email, password=self.password)


@pytest.fixture # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def authentication_client() -> AuthenticationClient:  # Аннотируем возвращаемое фикстурой значение
    return get_authentication_client() # Создаем новый API клиент для работы с аутентификацией

@pytest.fixture # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def public_users_client() -> PublicUsersClient:  # Аннотируем возвращаемое фикстурой значение
    return get_public_users_client()  # Создаем новый API клиент для работы с публичным API пользователей

@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient: # Аннотируем возвращаемое фикстурой значение
    return get_private_users_client(function_user.authentication_user) # Создаем новый API клиент для работы с приватным API пользователей, передавая данные аутентификации пользователя из фикстуры function_user


# Фикстура для создания пользователя
@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture: # Используем фикстуру public_users_client, которая создает нужный API клиент
    # подготовка и отправка запроса на создание пользователя
    request = CreateUserRequestSchema()
    # отправка запроса на создание пользователя с помощью метода create_user и данных запроса create_user_request
    response = public_users_client.create_user(request)
    return UserFixture(request = request, response = response) # возвращает экземпляр UserFixture, содержащий запрос и ответ на создание пользователя