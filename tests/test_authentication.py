from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from http import HTTPStatus

from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema



def test_login():
    # инициализация клиентов
    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()

    # подготовка и отправка запроса на создание пользователя
    create_user_request = CreateUserRequestSchema()

    # отправка запроса на создание пользователя с помощью метода create_user_api и данных запроса create_user_request
    create_user_response = public_users_client.create_user(create_user_request)

    # подготовка данных для аутентификации
    login_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )

    # отправка запроса на аутентификацию c помощью метода login_api и данных запроса login_request
    login_response = authentication_client.login_api(login_request)

    # десериализация JSON-ответа в LoginResponseSchema
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    # проверки ответа на аутентификацию
    assert_status_code(login_response.status_code, HTTPStatus.OK)  # проверка, что статус-код ответа соответствует ожидаемому (200 OK)
    assert_login_response(login_response_data)  # проверка, что ответ соответствует ожидаемому формату
    validate_json_schema(login_response.json(), login_response_data.model_json_schema())  # проверка, что ответ соответствует схеме LoginResponseSchema