from pydantic import BaseModel, Field, ConfigDict, EmailStr
from tools.fakers import fake


class UserSchema(BaseModel):  # создаем класс UserSchema, который наследуется от BaseModel для создания моделей данных с помощью Pydantic
    """
    Описание структуры пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)  # Настройка Pydantic для использования имен полей как по алиасу так и по имени

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):  # создаем класс CreateUserRequestSchema, который наследуется от BaseModel для создания моделей данных с помощью Pydantic:
    """
    Описание структуры запроса на создание пользователя.
    """
    model_config = ConfigDict(populate_by_name=True) # Настройка Pydantic для использования имен полей как по алиасу так и по имени

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(default_factory=fake.last_name, alias="lastName")
    first_name: str = Field(default_factory=fake.first_name, alias="firstName")
    middle_name: str = Field(default_factory=fake.middle_name, alias="middleName")


class CreateUserResponseSchema(BaseModel):  # создаем класс CreateUserResponseSchema, который наследуется от BaseModel для создания моделей данных с помощью Pydantic
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):  # создаем класс UpdateUserRequestSchema, который наследуется от BaseModel для создания моделей данных с помощью Pydantic
    """
    Описание структуры запроса на обновление пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)  # Настройка Pydantic для использования имен полей как по алиасу так и по имени

    email: EmailStr | None = Field(default_factory=fake.email)
    last_name: str | None = Field(default_factory=fake.last_name, alias="lastName")
    first_name: str | None = Field(default_factory=fake.first_name, alias="firstName")
    middle_name: str | None = Field(default_factory=fake.middle_name, alias="middleName")


class UpdateUserResponseSchema(BaseModel):  # создаем класс UpdateUserResponseSchema, который наследуется от BaseModel для создания моделей данных с помощью Pydantic
    """
    Описание структуры ответа обновления пользователя.
    """
    user: UserSchema


class GetUserResponseSchema(BaseModel):  # создаем класс GetUserResponseSchema, который наследуется от BaseModel для создания моделей данных с помощью Pydantic
    """
    Описание структуры ответа получения пользователя.
    """
    user: UserSchema