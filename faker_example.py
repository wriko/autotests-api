from faker import Faker

fake = Faker('ru-RU') # создание экземпляра класса Faker c указанием локали 'ru-RU'

# Генерация случайных данных
print(fake.name()) # Случайное имя
print(fake.address()) # Случайный адрес
print(fake.email())  #  Случайный email


data = {
    'name': fake.name(),
    'address': fake.address(),
    'email': fake.email(),
    'age': fake.random_int(min=18, max=99),  # Случайный возраст от 18 до 99
}
print(data)