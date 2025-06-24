# Пример использования JSON Schema для валидации данных

from jsonschema import validate

schema = {  # JSON Schema объект, описывающий структуру данных data
    "type": "object",
    "properties": {  # Свойства объекта
        "name": {  # Свойство name, строка
            "type": "string"  # Тип данных
        },
        "age": {  # Свойство age, целое число
            "type": "integer"  # Тип данных
        }
    },
    "required": ["name", "age"]  # Обязательные поля
}

data = {
    "name": "John Doe",
    "age": 30
}

validate(instance=data, schema=schema)  # Валидация данных data с помощью JSON Schema schema/ Ошибок не возникло, значит данные соответствуют схеме