from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True) # Настройка Pydantic для использования имен полей как по алиасу так и по имени

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса для получения списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)  # Настройка Pydantic для использования имен полей как по алиасу так и по имени

    user_id: str = Field(alias="userId")  # Используем alias для соответствия полю userId


class GetCoursesResponseSchema(BaseModel):
    """
    Описание структуры ответа для получения списка курсов.
    """
    courses: list[CourseSchema]


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)  # Настройка Pydantic для использования имен полей как по алиасу так и по имени

    title: str = Field(default_factory=fake.sentence) # Используем фабрику для генерации случайного заголовка курса
    max_score: int = Field(default_factory=fake.max_score, alias="maxScore")  # Используем фабрику для генерации случайного максимального балла и alias для соответствия полю maxScore
    min_score: int = Field(default_factory=fake.min_score,alias="minScore")  # Используем alias для соответствия полю minScore
    description: str = Field(default_factory=fake.text)  # Используем фабрику для генерации случайного описания курса
    estimated_time: str = Field(default_factory=fake.estimated_time, alias="estimatedTime")  # Используем фабрику для генерации случайного времени и alias для соответствия полю estimatedTime
    preview_file_id: str = Field(default_factory=fake.uuid4, alias="previewFileId")  # Используем фабрику для генерации случайного идентификатора файла превью и alias для соответствия полю previewFileId
    created_by_user_id: str = Field(default_factory=fake.uuid4, alias="createdByUserId")  #  Используем фабрику для генерации случайного идентификатора пользователя создателя и alias для соответствия полю createdByUserId


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)  # Настройка Pydantic для использования имен полей как по алиасу так и по имени

    title: str | None = Field(default_factory=fake.sentence)  # Используем фабрику для генерации случайного заголовка курса
    max_score: int | None = Field(default_factory=fake.max_score, alias="maxScore")  # Используем фабрику для генерации случайного максимального балла и alias для соответствия полю maxScore
    min_score: int | None = Field(default_factory=fake.min_score, alias="minScore")  #  Используем alias для соответствия полю minScore
    description: str | None = Field(default_factory=fake.text)  #  Используем фабрику для генерации случайного описания курса
    estimated_time: str | None = Field(default_factory=fake.estimated_time, alias="estimatedTime")  #  Используем фабрику для генерации случайного времени и alias для соответствия полю estimatedTime


class UpdateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления курса.
    """
    course: CourseSchema

