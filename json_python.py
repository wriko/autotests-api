import json

json_data = """
{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "courses": [
    "Python",
    "QA Automation",
    "API Testing"
  ],
  "address": {
    "city": "Москва",
    "zip": "101000"
  }
}
"""

# --------------------------------------------------------
# ПРЕОБРАЗОВАНИЕ JSON В СЛОВАРЬ !!!!!!!!!!
# --------------------------------------------------------
# Для преобразования JSON в словарь используется функция `json.loads()`, которая принимает строку в формате JSON и возвращает соответствующий словарь Python.
parsed_data = json.loads(json_data)

# print(parsed_data)
# print(parsed_data['courses'])  # возвращает список курсов по указанному ключу словаря

data = {
    "name": "Иван",
    "age": 30,
    "is_student": False
}

# --------------------------------------------------------
# ПРЕОБРАЗОВАНИЕ СЛОВАРЯ В  JSON
# --------------------------------------------------------
json_string = json.dumps(data, indent=4)  # используется функция `json.dumps()`. Параметр `indent=4` указывает, что в результате получится красиво отформатированный JSON с отступами в 4 пробела.
print(json_string)

# --------------------------------------------------------
# ЧТЕНИЕ ДАННЫХ ИЗ ФАЙЛА JSON
# --------------------------------------------------------
with open("json_example.json", "r", encoding="utf-8" ) as file:
    data = json.load(file)
    print(data)

# --------------------------------------------------------
# ЗАПИСЬ ДАННЫХ В ФАЙЛ JSON
# --------------------------------------------------------
with open("output.json", "w", encoding="utf-8") as file: # Открываем файл для записи
    json.dump(data, file, indent=2, ensure_ascii=False)  # Записываем данные в файл с отступами, в файл кладем словарь `data`. ensure_ascii # используется для того, чтобы сохранить символы в читаемом виде (например, кириллицу) вместо их экранирования.
    print("Данные успешно записаны в файл output.json")