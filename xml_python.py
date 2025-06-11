import xml.etree.ElementTree as ET # Импортируем модуль для работы с XML

xml_data = """
<user>
    <id>1</id>
    <name>John Doe</name>
    <age>30</age>
    <email>ww@ww.ru</email>
</user>
"""

# Парсим XML данные
root = ET.fromstring(xml_data)
print("User ID:", root.find('id').text) # Выводим значение элемента <id>
print("User Name:", root.find('name').text) # Выводим значение элемента <name>
print("User Email:", root.find('email').text)  # Выводим значение элемента <email>