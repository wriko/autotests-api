from pydantic import BaseModel, Field
from tools.fakers import fake

class TokenSchema(BaseModel): # создаем модель данных для токена авторизации, наследуясь от BaseModel Pydantic
    """
    Описание структуры токена аутентификации.
    """
    token_type: str = Field(alias="tokenType", description="Тип токена") # ключ tokenType должен быть строкой
    access_token: str = Field(alias="accessToken", description="Токен доступа") # ключ accessToken должен быть строкой
    refresh_token: str = Field(alias="refreshToken", description="Токен обновления") # ключ refreshToken должен быть строкой


class LoginRequestSchema(BaseModel): # создаем модель данных для запроса авторизации, наследуясь от BaseModel Pydantic
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str = Field(default_factory=fake.email) # ключ email должен быть строкой, по умолчанию используется функция fake.email() для генерации случайного email
    password: str = Field(default_factory=fake.password)  # ключ password должен быть строкой, по умолчанию используется функция fake.password() для генерации случайного пароля


class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос аутентификации.
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel): # создаем словарь с фиксированными ключами и типами значений для запроса обновления токена
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence()) # ключ refreshToken должен быть строкой, по умолчанию используется функция fake.sentence() для генерации случайной строки
