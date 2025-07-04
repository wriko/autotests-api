from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, GetUserResponseSchema
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


def assert_user(actual: UserSchema, expected: UserSchema): # на входе принимает ответ на получение пользователя и ожидаемые данные пользователя
    """
    Проверяет, что данные пользователя соответствуют ожиданиям.

    :param actual: Ответ API c данными пользователя.
    :param expected: Ожидаемые данные пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, name="id")
    assert_equal(actual.email, expected.email, name="email")
    assert_equal(actual.last_name, expected.last_name, name="last_name")
    assert_equal(actual.first_name, expected.first_name, name="first_name")
    assert_equal(actual.middle_name, expected.middle_name, name="middle_name")


def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema): # на входе принимает ответ на получение пользователя и ответ на создание пользователя
    """
    Проверяет, что ответ на получение пользователя соответствует ответу на создание пользователя.

    :param get_user_response: Ответ API на получение пользователя.
    :param create_user_response: Ответ API на создание пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_user(get_user_response.user, create_user_response.user)