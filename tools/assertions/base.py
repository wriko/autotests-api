from typing import Any

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