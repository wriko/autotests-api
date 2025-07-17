from http import HTTPStatus

import pytest
from allure_commons.types import Severity

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, GetCoursesQuerySchema, \
    GetCoursesResponseSchema, CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response, \
    assert_create_course_response
from tools.assertions.schema import validate_json_schema
import allure


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)  # статическая аннотация для allure, которая задает эпик для класса. Берутся из Enam AllureEpic
@allure.feature(AllureFeature.COURSES)  # статическая аннотация для allure, которая задает фичу для класса. Берутся из Enam AllureFeature
class TestCourses:
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Cоздание курса")
    @allure.severity(Severity.BLOCKER)  # статическая аннотация для allure, которая задает важность теста. Берутся из Enam Severity
    def test_create_course(
            self,
            courses_client: CoursesClient, # CoursesClient - фикстура, предоставляющая клиент для работы с курсами
            function_user: UserFixture, # UserFixture - фикстура, создающая тестового пользователя и возвращающая его данные
            function_file: FileFixture # FileFixture - фикстура, создающая тестовый файл и возвращающая его данные
    ):
        # Создаем объект запроса на создание курса, заполняя его поля данными из фикстуры (генерируемых данных default-factory), preview_file_id и created_by_user_id берем реальные их ответов на создание пользователя и файла
        request = CreateCourseRequestSchema(preview_file_id=function_file.response.file.id, created_by_user_id=function_user.response.user.id)
        # POST-запрос к эндпоинту /api/v1/courses, используя API-клиент CoursesClient.create_course_api
        response = courses_client.create_course_api(request)

        # Проверяем, что ответ от сервера соответствует ожидаемой структуре (Pydantic-схеме).
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)
        # Проверяем, что статус ответа равен HTTPStatus.OK (200)
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем соответствие данных запроса и ответа (например, поля title, description и т.д.)
        assert_create_course_response(request, response_data)
        # Проверяем, что JSON-структура ответа соответствует ожидаемой схеме
        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title("Получение курсов по пользователю")
    @allure.severity(Severity.BLOCKER)
    def test_get_courses(
            self,
            courses_client: CoursesClient, # CoursesClient - фикстура, предоставляющая клиент для работы с курсами
            function_user: UserFixture, # UserFixture - фикстура, создающая тестового пользователя и возвращающая его данные
            function_course: CourseFixture # CourseFixture - фикстура, создающая тестовый курс и возвращающая его данные
    ):
        # Создаем объект запроса на получение курсов, передавая в query параметр user_id (из фикстуры function_user)
        query = GetCoursesQuerySchema(user_id=function_user.response.user.id)
        # Отправляем GET-запрос на получение списка курсов
        response = courses_client.get_courses_api(query)

        # Проверяем, что ответ от сервера соответствует ожидаемой структуре (Pydantic-схеме).
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)
        # Проверяем, что статус ответа равен HTTPStatus.OK (200)
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что список курсов соответствует ранее созданным курсам
        assert_get_courses_response(response_data, [function_course.response])
        # Проверяем, что JSON-структура ответа соответствует ожидаемой схеме
        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.title("Обновление курса")
    @allure.severity(Severity.CRITICAL)
    def test_update_course(self, courses_client: CoursesClient, function_course: CourseFixture): # CoursesClient - фикстура, предоставляющая клиент для работы с курсами, CourseFixture - фикстура, создающая тестовый курс и возвращающая его данные
        # Создаем объект запроса на обновление курса, заполняя его поля данными из фикстуры (генерируемых данных default-factory)
        request = UpdateCourseRequestSchema(title="123")
        # Отправляем PATCH-запрос на сервер для обновления курса по его ID.
        response = courses_client.update_course_api(function_course.response.course.id, request) # # Используем ID курса из фикстуры, request-  Передаем данные запроса

        # Проверяем, что ответ от сервера соответствует ожидаемой структуре (Pydantic-схеме).
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)
        # Проверяем, что статус ответа равен HTTPStatus.OK (200)
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем соответствие данных запроса и ответа (например, поля title, description и т.д.)
        assert_update_course_response(request, response_data)
        # Проверяем, что JSON-структура ответа соответствует ожидаемой схеме
        validate_json_schema(response.json(), response_data.model_json_schema())