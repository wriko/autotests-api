from http import HTTPStatus

import pytest
from allure_commons.types import Severity

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseResponseSchema, \
    GetExercisesQuerySchema, UpdateExerciseRequestSchema, GetExercisesResponseSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema
import allure


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)  # статическая аннотация для allure, которая задает эпик для класса. Берутся из Enam AllureEpic
@allure.feature(AllureFeature.EXERCISES)  # статическая аннотация для allure, которая задает фичу для класса. Берутся из Enam AllureFeature
class TestExercises:
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title('Создание задания')
    @allure.severity(Severity.BLOCKER)
    def test_create_exercise(
            self,
            exercises_client: ExercisesClient,  # фикстура, предоставляющая клиент для работы с заданиями
            function_course: CourseFixture      # фикстура, создающая курс и возвращающая его данные (нужен будет course_id)
    ):
        # Создаем объект запроса на создание задания
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        # POST-запрос к эндпоинту /api/v1/exercises, используя API-клиент ExercisesClient.create_exercise_api
        response = exercises_client.create_exercise_api(request)

        # Проверяем, что ответ от сервера соответствует ожидаемой структуре (Pydantic-схеме).
        response_data = ExerciseResponseSchema.model_validate_json(response.text)
        # Проверяем, что статус ответа равен HTTPStatus.OK (200)
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверьте, что тело ответа соответствует запросу на создание задания
        assert_create_exercise_response(request, response_data)
        # Проверяем, что JSON-структура ответа соответствует ожидаемой схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title('Получение задания')
    @allure.severity(Severity.BLOCKER)
    def test_get_exercise(
            self,
            exercises_client: ExercisesClient,  # фикстура, предоставляющая клиент для работы с заданиями
            function_exercise: ExerciseFixture  # фикстура, создающая задание и возвращающая его данные (нужен будет exercise_id)
    ):
        # Отправляем GET-запрос на получение ифнормации о задании по его exercise_id
        response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)

        # Проверяем, что ответ от сервера соответствует ожидаемой структуре (Pydantic-схеме).
        response_data = ExerciseResponseSchema.model_validate_json(response.text)
        # Проверяем, что статус ответа равен HTTPStatus.OK (200)
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что ответ c данными задания соответствует запросу на создание задания
        assert_get_exercise_response(response_data, function_exercise.response)
        # Проверяем, что JSON-структура ответа соответствует ожидаемой схеме
        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.title('Обновление задания')
    @allure.severity(Severity.CRITICAL)
    def test_update_exercise(
            self,
            exercises_client: ExercisesClient,  # фикстура, предоставляющая клиент для работы с заданиями
            function_exercise: ExerciseFixture  # фикстура, создающая задание и возвращающая его данные
    ):
        # Создаем объект запроса на обновление задания, заполняя его поля данными из фикстуры (генерируемых данных default-factory)
        request = UpdateExerciseRequestSchema()
        # Выполняем PATCH-запрос к эндпоинту /api/v1/exercises/{exercise_id}, exercise_id получаем из фикстуры function_exercise
        response = exercises_client.update_exercise_api(exercise_id=function_exercise.response.exercise.id, request=request)

        # Проверяем, что ответ от сервера соответствует ожидаемой структуре (Pydantic-схеме).
        response_data = ExerciseResponseSchema.model_validate_json(response.text)
        # Проверяем, что статус ответа равен HTTPStatus.OK (200)
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что тело ответа соответствует запросу на обновление задания
        assert_update_exercise_response(request, response_data)
        # Проверяем, что JSON-структура ответа соответствует ожидаемой схеме
        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.title('Удаление задания')
    @allure.severity(Severity.CRITICAL)
    def test_delete_exercise(
            self,
            exercises_client: ExercisesClient,  # фикстура, предоставляющая клиент для работы с заданиями
            function_exercise: ExerciseFixture  # фикстура, создающая задание и возвращающая его данные
    ):
        # Отправляем DELETE-запрос на удаление задания по его exercise_id, exercise_id получаем из фикстуры function_exercise
        response = exercises_client.delete_exercise_api(exercise_id=function_exercise.response.exercise.id)

        # Проверяем, что статус ответа равен HTTPStatus.OK (200)
        assert_status_code(response.status_code, HTTPStatus.OK)

        # Проверяем, что задание удалено
        get_exercise_response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        # Проверяем, что ответ от сервера соответствует ожидаемой структуре (Pydantic-схеме).
        get_exercise_response_data = InternalErrorResponseSchema.model_validate_json(get_exercise_response.text)
        # Проверяем, что статус ответа равен HTTPStatus.NOT_FOUND (404)
        assert_status_code(get_exercise_response.status_code, HTTPStatus.NOT_FOUND)

        # Проверяем, что тело ответа на запрос на получение задания по его id равно 404 Exercise not found
        assert_exercise_not_found_response(get_exercise_response_data)
        # Проверяем, что JSON-структура ответа соответствует ожидаемой схеме
        validate_json_schema(get_exercise_response.json(), get_exercise_response_data.model_json_schema())


    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title('Получение списка заданий')
    @allure.severity(Severity.BLOCKER)
    def test_get_exercises(
            self,
            exercises_client: ExercisesClient,  # фикстура, предоставляющая клиент для работы с заданиями
            function_course: CourseFixture,  # фикстура, создающая курс и возвращающая его данные
            function_exercise: ExerciseFixture # фикстура, создающая задание и возвращающая его данные
    ):
        # Создаем объект запроса на получение заданий по course_id, передавая в query параметр course_id (из фикстуры function_course)
        query = GetExercisesQuerySchema(course_id=function_course.response.course.id)
        # Отправляем GET-запрос на получение списка заданий по course_id
        response = exercises_client.get_exercises_api(query)

        # Проверяем, что ответ от сервера соответствует ожидаемой структуре (Pydantic-схеме).
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        # Проверяем, что статус ответа равен HTTPStatus.OK (200)
        assert_status_code(response.status_code, HTTPStatus.OK)

        # Проверяем, что список заданий соответствует ранее созданным заданиям
        assert_get_exercises_response(response_data, [function_exercise.response])

        # Проверяем, что JSON-структура ответа соответствует ожидаемой схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

