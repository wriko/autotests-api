from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
import allure
from tools.logger import get_logger



logger = get_logger("ERRORS_ASSERTIONS")



@allure.step("Проверка ошибки валидации")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Проверяет, что объект ошибки валидации соответствует ожидаемому значению.

    :param actual: Фактическая ошибка.
    :param expected: Ожидаемая ошибка.
    :raises AssertionError: Если объекты не соответствуют.
    """
    logger.info("Проверка ошибки валидации")

    assert_equal(actual.type, expected.type, name="type")
    assert_equal(actual.input, expected.input, name="input")
    assert_equal(actual.context, expected.context, name="context")
    assert_equal(actual.message, expected.message, name="message")
    assert_equal(actual.location, expected.location, name="location")


@allure.step("Проверка ошибки из ответа")
def assert_validation_error_response(actual: ValidationErrorResponseSchema, expected: ValidationErrorResponseSchema):
    """
    Проверяет, что объект ответа API с ошибками валидации (ValidationErrorResponseSchema) соответствует ожидаемому значению.

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если объекты не соответствуют.
    """
    logger.info("Проверка ошибки из ответа")

    assert_length(actual.details, expected.details, name="details")

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)


@allure.step("Проверка внутренней ошибки из ответа")
def assert_internal_error_response(actual: InternalErrorResponseSchema, expected: InternalErrorResponseSchema):
    """
    Функция для проверки внутренней ошибки. Например 404 File not found

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если объекты не соответствуют.
    """
    logger.info("Проверка внутренней ошибки из ответа")

    assert_equal(actual.details, expected.details, name="details")