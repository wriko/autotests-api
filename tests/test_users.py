import pytest

from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus

from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response


@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient): # Инициализация клиента public_users_client с помощью фикстуры, которая возвращает экземпляр PublicUsersClient
    request = CreateUserRequestSchema()  # создание запроса на создание пользователя c помощью схемы CreateUserRequestSchema (aтрибуты будут заполнены случайными фейковыми значениями)
    response = public_users_client.create_user_api(request)  # отправка запроса на создание пользователя c помощью метода create_user_api (для анализа Response)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)  # преобразование ответа в словарь с данными пользователя с помощью метода model_value_json класса CreateUserResponseSchema

    assert_status_code(response.status_code, HTTPStatus.OK)  # проверка, что статус ответа равен 200 (успешное создание пользователя)
    assert_create_user_response(request, response_data)  # проверка, что ответ соответствует запросу на создание пользователя

    validate_json_schema(response.json(), response_data.model_json_schema())  #  проверка, что ответ соответствует схеме CreateUserResponseSchema


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(function_user: UserFixture, private_users_client: PrivateUsersClient): # Инициализация клиента private_users_client с помощью фикстуры, которая возвращает экземпляр PrivateUsersClient
    response = private_users_client.get_user_me_api()  # отправка запроса на получение текущего пользователя c помощью метода get_user_me_api (для анализа Response)
    response_data = GetUserResponseSchema.model_validate_json(response.text)  # преобразование ответа в словарь с данными пользователя с помощью метода model_value_json класса CreateUserResponseSchema

    assert_status_code(response.status_code, HTTPStatus.OK)  # проверка, что статус ответа равен 200 (успешное создание пользователя)
    assert_get_user_response(response_data, function_user.response) # проверка, что ответ соответствует запросу на создание пользователя. response_data - это ответ на получение пользователя, а function_user.response - это ответ на создание пользователя

    validate_json_schema(response.json(), response_data.model_json_schema()) #  проверка, что ответ соответствует схеме GetUserResponseSchema