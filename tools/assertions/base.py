from typing import Any, Sized
import allure




@allure.step("Проверяем что статус-код ответа соответствует {expected}")
def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус-код ответа.
    :raises AssertionError: Если фактический статус-код не соответствует ожидаемому.
    """
    assert actual == expected, (
        "Некорректный статус-код ответа."
        f" Ожидался {expected}, получен {actual}."
    )


@allure.step("Проверяем что {name} соответствует {actual}")
def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение соответствует ожидаемому значению.

    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :param name: Название проверяемого параметра.
    :raises AssertionError: Если фактическое значение не соответствует ожидаемому.
    """
    assert actual == expected, (
        f"Некорректное значение {name}."
        f" Ожидалось {expected}, получено {actual}."
    )


@allure.step("Проверяем что {name} истинно")
def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что фактическая длина объекта соответствует ожидаемой.

    :param actual: Фактическая длина объекта.
    :param expected: Ожидаемая длина объекта.
    :param name: Название проверяемого объекта.
    :raises AssertionError: Если длины не совпадают.
    """
    with allure.step(f"Проверяем что длина  {name} соответствует {len(expected)}"):
        assert len(actual) == len(expected), (f"Некорректная длина обекта {name}. Ожидалось {len(expected)}, получено {len(actual)}")