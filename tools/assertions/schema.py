from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator

def validate_json_schema(instance: Any, schema: dict):
    """
    Функция для валидации JSON схемы с использованием jsonschema.

    :param instance: JSON объект, который нужно проверить
    :param schema: JSON схема, против которой нужно проверить объект
    :param format_checker: Проверка формата данных

    :return: None, если валидация прошла успешно
    """
    validate(instance=instance, schema=schema, format_checker=Draft202012Validator.FORMAT_CHECKER) # проверяем, что валидация схемы прошла успешно format_checker=Draft202012Validator.FORMAT_CHECKER - проверка формата данных