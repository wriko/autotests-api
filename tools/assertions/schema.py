from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator
import allure
from tools.logger import get_logger



logger = get_logger("SCHEMA_ASSERTIONS")




@allure.step("Валидация JSON схемы")
def validate_json_schema(instance: Any, schema: dict):
    """
    Функция для валидации JSON схемы с использованием jsonschema.

    :param instance: JSON объект, который нужно проверить
    :param schema: JSON схема, против которой нужно проверить объект
    :param format_checker: Проверка формата данных

    :return: None, если валидация прошла успешно
    """
    logger.info("Валидация JSON схемы")

    validate(instance=instance, schema=schema, format_checker=Draft202012Validator.FORMAT_CHECKER) # проверяем, что валидация схемы прошла успешно format_checker=Draft202012Validator.FORMAT_CHECKER - проверка формата данных