from pydantic import BaseModel, Field


class Address(BaseModel):  # создание модели адреса
    city: str
    zip_code: str


class User(BaseModel):  # создание модели пользователя
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = True


user = User( # создание экземпляра модели
    id = 1,
    name = 'John',
    email = 'john@example.com',
    address = Address(city = 'New York', zip_code = '10001')
)
print(user)

# как из модели сделать словарь
print(user.model_dump())

# как из модели сделать JSON строку
print(user.model_dump_json())


# аллиасы

class User2(BaseModel):  # создание модели пользователя
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = Field(alias="isActive") # переименование поля в JSON. Если придет  isActive - то будет взято значение is_active


user_data = {
    "id": 1,
    "name": "John",
    "email": "john@example.com",
    "address": {
        "city": "New York",
        "zip_code": "10001"
        },
    'isActive': True # pydantic возьмет его из алиаса
}

user2 = User2(**user_data) # создание экземпляра модели
print(user2.model_dump()) # {'id': 1, 'name': 'John', 'email': 'john@example.com', 'address': {'city': 'New York', 'zip_code': '10001'}, 'is_active': True}
