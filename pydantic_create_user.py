from pydantic import BaseModel, Field, EmailStr, UUID4, constr


class UserSchema(BaseModel):
    """
    Схема данных пользователя, возвращаемая в ответе или используемая внутри системы.

    Атрибуты:
        id (str): Уникальный идентификатор пользователя.
        email (EmailStr): Адрес электронной почты.
        lastName (str): Фамилия пользователя.
        firstName (str): Имя пользователя.
        middleName (str): Отчество пользователя.
    """
    id: UUID4
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Схема запроса на создание пользователя.

    Атрибуты:
        email (EmailStr): Адрес электронной почты.
        password (str): Пароль пользователя.
        lastName (str): Фамилия пользователя.
        firstName (str): Имя пользователя.
        middleName (str): Отчество пользователя.
    """
    email: EmailStr
    password: constr = Field(min_length=3, description="Минимальная длина пароля - 3 символа")
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа при успешном создании пользователя.

    Атрибуты:
        user (UserSchema): Схема данных пользователя.
    """
    user: UserSchema
