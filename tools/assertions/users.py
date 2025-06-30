from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(resuest: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param resuest: Запрос на создание пользователя.
    :param response: Ответ API c данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, resuest.email, name="email")
    assert_equal(response.user.last_name, resuest.last_name, name="last_name")
    assert_equal(response.user.first_name, resuest.first_name, name="first_name")
    assert_equal(response.user.middle_name, resuest.middle_name, name="middle_name")
