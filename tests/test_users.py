from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus

from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response


def test_create_user():
    public_users_client = get_public_users_client()  # инициализация клиента созданием пользователя

    request = CreateUserRequestSchema()  # создание запроса на создание пользователя c помощью схемы CreateUserRequestSchema (aтрибуты будут заполнены случайными фейковыми значениями)
    response = public_users_client.create_user_api(request)  # отправка запроса на создание пользователя c помощью метода create_user_api (для анализа Response)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)  # преобразование ответа в словарь с данными пользователя с помощью метода model_value_json класса CreateUserResponseSchema

    assert_status_code(response.status_code, HTTPStatus.OK)  # проверка, что статус ответа равен 200 (успешное создание пользователя)
    assert_create_user_response(request, response_data)  # проверка, что ответ соответствует запросу на создание пользователя

    validate_json_schema(response.json(), response_data.model_json_schema())  #  проверка, что ответ соответствует схеме CreateUserResponseSchema