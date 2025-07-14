from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseResponseSchema, \
    GetExercisesQuerySchema, UpdateExerciseRequestSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
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


    def test_update_exercise(
            self,
            exercises_client: ExercisesClient,  # фикстура, предоставляющая клиент для работы с заданиями
            function_exercise: ExerciseFixture  # фикстура, создающая задание и возвращающая его данные
    ):
        # Создаем объект запроса на обновление задания, заполняя его поля данными из фикстуры (генерируемых данных default-factory)
        request = UpdateExerciseRequestSchema()
        # Выполняем PATCH-запрос к эндпоинту /api/v1/exercises/{exercise_id}, exercise_id получаем из фикстуры function_exercise
        response = exercises_client.update_exercise_api(function_exercise.response.exercise.id, request)

        # Проверяем, что ответ от сервера соответствует ожидаемой структуре (Pydantic-схеме).
        response_data = ExerciseResponseSchema.model_validate_json(response.text)
        # Проверяем, что статус ответа равен HTTPStatus.OK (200)
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что тело ответа соответствует запросу на обновление задания
        assert_update_exercise_response(request, response_data)
        # Проверяем, что JSON-структура ответа соответствует ожидаемой схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

