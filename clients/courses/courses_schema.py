from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True) # Настройка Pydantic для использования имен полей как по алиасу так и по имени

    id: str
    title: str
    max_score: int = Field(alias="maxScore")  # Используем alias для соответствия полю maxScore
    min_score: int = Field(alias="minScore")  # Используем alias для соответствия полю minScore
    description: str
    preview_file: FileSchema = Field(alias="previewFile")  # Используем alias для соответствия полю previewFileId
    estimated_time: str = Field(alias="estimatedTime") # Используем alias для соответствия полю estimatedTime
    created_by_user: UserSchema = Field(alias="createdByUser")  # Используем alias для соответствия полю createdByUserId


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса для получения списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)  # Настройка Pydantic для использования имен полей как по алиасу так и по имени

    user_id: str = Field(alias="userId")  # Используем alias для соответствия полю userId


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)  # Настройка Pydantic для использования имен полей как по алиасу так и по имени

    title: str
    max_score: int = Field(alias="maxScore")  # Используем alias для соответствия полю maxScore
    min_score: int = Field(alias="minScore")  # Используем alias для соответствия полю minScore
    description: str
    estimated_time: str = Field(alias="estimatedTime")  # Используем alias для соответствия полю estimatedTime
    preview_file_id: str = Field(alias="previewFileId")  # Используем alias для соответствия полю previewFileId
    created_by_user_id: str = Field(alias="createdByUserId")  # Используем alias для соответствия полю createdByUserId


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

    title: str | None
    max_score: int | None = Field(alias="maxScore")  # Используем alias для соответствия полю maxScore
    min_score: int | None = Field(alias="minScore")  # Используем alias для соответствия полю minScore
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")  # Используем alias для соответствия полю estimatedTime
