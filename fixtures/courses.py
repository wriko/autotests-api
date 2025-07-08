from clients.courses.courses_client import CoursesClient, get_courses_client
import pytest
from pydantic import BaseModel
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema

from fixtures.users import UserFixture
from fixtures.files import FilesFixture


class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema #  содержит данные запроса на создание курса (CreateCourseRequestSchema).
    response: CreateCourseResponseSchema # содержит ответ API после создания курса (CreateCourseResponseSchema).

# Эта фикстура создает клиент CoursesClient, который используется для взаимодействия с API курсов.
@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient: # В аргумент передается function_user — фикстура, предоставляющая тестового пользователя.
    return get_courses_client(function_user.authentication_user) # Используется get_courses_client, который создает и возвращает объект CoursesClient, уже аутентифицированный от имени данного пользователя.

# Эта фикстура создает тестовый курс перед выполнением теста и возвращает объект с данными созданного курса.
@pytest.fixture
def function_course(courses_client: CoursesClient, function_user: UserFixture, function_file: FilesFixture) -> CourseFixture: # — клиент для работы с API курсов.  пользователь, от имени которого создается курс.  загруженный файл, который будет использоваться в качестве изображения превью курса.
    request = CreateCourseRequestSchema() # Создается объект request типа CreateCourseRequestSchema, содержащий preview_file_id — идентификатор файла (из function_file), который будет использоваться как изображение для курса. created_by_user_id — идентификатор пользователя, создавшего курс
    response = courses_client.create_course(request) # Затем courses_client.create_course(request) отправляет запрос на создание курса в API.
    return CourseFixture(request=request, response=response) # После успешного создания курса возвращается объект CourseFixture, содержащий запрос и ответ API.
