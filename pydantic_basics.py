"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""

import uuid
from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError


from pydantic.alias_generators import to_camel


# задание модели данных файла (схема)
class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl # проверка на корректность url


# задание модели данных пользователя (схема)
class UserSchema(BaseModel):
    id: str
    email: EmailStr  # EmailStr - проверка на корректность email
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    # если необходимо добавить вычисляемое поле:
    @computed_field  # вычисление полей
    def username(self) -> str:
        return f"{self.last_name} {self.first_name}"
    # или так
    def get_user_name(self) -> str:  # метод для получения имени пользователя
        return f"{self.last_name} {self.first_name}"


# задание модели данных курса (схема)
class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)  # to_camel - генератор алиасов для модели и populate_by_name - заполнение полей по имени, а не только по алиасу

    id: str = Field(default_factory=lambda: str(uuid.uuid4())) # default_factory - генератор значений uuid
    title: str = "Playwrigth"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwrigth course"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")



# инициализация модели данных курса

course_default_model = CourseSchema(
    id ="course_id",
    title = "Playwrigth",
    maxScore = 100,
    minScore = 10,
    description = "Playwrigth",
    previewFile = FileSchema(
        id = "file-id",
        url = "http://localhost:8000/",
        filename = "images.png",
        directory = "courses"
    ),
    estimatedTime = "1 week",
    createdByUser = UserSchema(
        id = "user-id",
        email = "user@example.com",
        lastName = "Ivanov",
        firstName = "Ivan",
        middleName = "Ivanovich"
    )
)

print(f"Course_default_model:  {course_default_model}")



# десериализация Инициализация через словарь

course_dict = {
    "id": "course_id",
    "title": "Playwrigth",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwrigth",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000/",
        "filename": "images.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@example.com",
        "lastName": "Ivanov",
        "firstName": "Ivan",
        "middleName": "Ivanovich"
    }
}

# инициализируем и  распакуем словарь в модель данных для курса
course_dict_model = CourseSchema(**course_dict)
print(f"Course_dict_model:  {course_dict_model}")


# десериализация.Инициализация через JSON-строку

course_json = """
{
    "id": "course_id",
    "title": "Playwrigth",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwrigth",
    "previewFile": {"id": "file-id", "url": "http://localhost:8000/", "filename": "images.png", "directory": "courses" },
    "estimatedTime": "1 week",
    "createdByUser": {"id": "user-id","email": "user@example.com", "lastName": "Ivanov", "firstName": "Ivan", "middleName": "Ivanovich"}
}
"""

course_json_model = CourseSchema.model_validate_json(course_json) # CourseSchema.model_validate_json - метод для валидации JSON-строки по модели данных для курса
print(f"Course_json_model:  {course_json_model}")



print("---------------------------------------------------------------------------------------------------------------")
print("ЧТО БЫЛО ВЫШЕ В КОДЕ?")
print("---------------------------------------------------------------------------------------------------------------")

# АЛИАСЫ
# импортируем Field из pydantic
# from pydantic import BaseModel, Field
# и изменим базовую схему на алиасы

class NewCourseSchema(BaseModel):
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


new_course_json = """
{
    "id": "course_id",
    "title": "Playwrigth",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwrigth",
    "estimatedTime": "1 week"
}
"""

new_course_json_model = NewCourseSchema.model_validate_json(new_course_json) # CourseSchema.model_validate_json - метод для валидации JSON-строки по модели данных для курса
print(f"NEW Course_json_model:  {new_course_json_model}")


# сериализация. Из модели данных в JSON-строку или словарь

print(f"сериализация модели данных в JSON-строку:  {new_course_json_model.model_dump_json(by_alias=True)}") # model_dump_json - метод для сериализации модели данных в JSON-строку
print(f"сериализация модели данных в словарь:  {new_course_json_model.model_dump(by_alias=True)}") # model_dump - метод для сериализации модели данных в словарь


# использование pydantic alias generators
# импортируем to_camelиз pydantic.alias_generators
# и ConfigDict из pydantic

class ConfigCourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True) # to_camel - генератор алиасов для модели и populate_by_name - заполнение полей по имени а не только по алиасу

    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    estimated_time: str


config_course_json = """
{
    "id": "course_id",
    "title": "Playwrigth",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwrigth",
    "estimatedTime": "1 week"
}
"""


config_course_json_model = ConfigCourseSchema.model_validate_json(config_course_json) # CourseSchema.model_validate_json - метод для валидации JSON-строки по модели данных для курса
print(f"CONFIG Course_json_model:  {config_course_json_model}")


# значения по умолчанию

class DefaulCourseSchema(BaseModel):

    id: str = "course_id"
    title: str = "Playwrigth"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwrigth course"
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")

course = DefaulCourseSchema()
print(f"Course:  {course}")


# использование default_factory !!!!!!!!!!!!!!!

class DFCourseSchema(BaseModel):

    id: str = Field(default_factory=lambda: str(uuid.uuid4())) # default_factory - генератор значений uuid
    title: str = "Playwrigth"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwrigth course"
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")

course = DFCourseSchema()
print(f"Course1:  {course.id}")


# обработка ошибок !!!!!!!!!!!!!!!!
# импортируем ValidationError из pydantic
# Инициализируем FileSchema c некорректным url

try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="images.png",
        directory="courses"
    )
except ValidationError as error:
    print(f"ERROR:  {error}")   # JSON-строка с ошибками
    print(f"ERRORS:  {error.errors()}") # список ошибок валидации






