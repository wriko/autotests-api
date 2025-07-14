from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseResponseSchema, ExerciseSchema, \
    UpdateExerciseRequestSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(request: CreateExerciseRequestSchema, response: ExerciseResponseSchema):
    """
    Проверяет, что ответ на создание задания соответствует данным из запроса.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API c данными созданного задания.
    :raise AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.exercise.title, request.title, name="title")
    assert_equal(response.exercise.course_id, request.course_id, name="course_id")
    assert_equal(response.exercise.max_score, request.max_score, name="max_score")
    assert_equal(response.exercise.min_score, request.min_score, name="min_score")
    assert_equal(response.exercise.order_index, request.order_index, name="order_index")
    assert_equal(response.exercise.description, request.description, name="description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, name="estimated_time")


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные задания соответствуют ожиданиям.

    :param actual: Фактические данные задания.
    :param expected: Ожидаемые данные задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, name="id")
    assert_equal(actual.title, expected.title, name="title")
    assert_equal(actual.course_id, expected.course_id, name="course_id")
    assert_equal(actual.max_score, expected.max_score, name="max_score")
    assert_equal(actual.min_score, expected.min_score, name="min_score")
    assert_equal(actual.order_index, expected.order_index, name="order_index")
    assert_equal(actual.description, expected.description, name="description")
    assert_equal(actual.estimated_time, expected.estimated_time, name="estimated_time")


def assert_get_exercise_response(get_exercise_response: ExerciseResponseSchema, create_exercise_response: ExerciseResponseSchema):
    """
    Проверяет, что ответ на получение данных задания соответствует ответу на создание задания.

    :param get_exercise_response: Ответ API на получение данных задания.
    :param create_exercise_response: Ответ API на создание задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)


def assert_update_exercise_response(request: UpdateExerciseRequestSchema, response: ExerciseResponseSchema):
    """
    Проверяет, что ответ на обновление задания соответствует данным из запроса.

    :param request: Исходный запрос на обновление задания.
    :param response: Ответ API c обновленными данными задания.
    :raise AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.exercise.title, request.title, name="title")
    assert_equal(response.exercise.max_score, request.max_score, name="max_score")
    assert_equal(response.exercise.min_score, request.min_score, name="min_score")
    assert_equal(response.exercise.order_index, request.order_index, name="order_index")
    assert_equal(response.exercise.description, request.description, name="description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, name="estimated_time")