from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema




class ExerciseSchema(BaseModel):
    """
    Описание структуры задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий для определенного курса.
    """
    model_config = ConfigDict(populate_by_name=True) # Настройка Pydantic для использования имен полей как по алиасу так и по имени поля в классе.

    course_id: str = Field(alias="courseId") # Используем alias для соответствия полю courseId в запросе и полю course_id в классе.


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка заданий для определенного курса.
    """
    exercises: list[ExerciseSchema]


class ExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение информации о задании по exercise_id.
    """
    exercise: ExerciseSchema


class CreateExerciseRequestSchema(BaseModel): # Тип словаря с данными для создания задания. Принимает: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
    """
    Описание структуры запроса на создание задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class UpdateExerciseRequestSchema(BaseModel): # Тип словаря с данными для обновления задания. Принимает: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
    """
    Описание структуры запроса на обновление задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None = Field(alias="description")
    estimated_time: str | None = Field(alias="estimatedTime")