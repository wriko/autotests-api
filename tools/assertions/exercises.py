from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseResponseSchema, ExerciseSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response
import allure
from tools.logger import get_logger



logger = get_logger("EXERCISES_ASSERTIONS")




@allure.step("Проверка ответа на создание задания")
def assert_create_exercise_response(request: CreateExerciseRequestSchema, response: ExerciseResponseSchema):
    """
    Проверяет, что ответ на создание задания соответствует данным из запроса.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API c данными созданного задания.
    :raise AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Проверка ответа на создание задания")

    assert_equal(response.exercise.title, request.title, name="title")
    assert_equal(response.exercise.course_id, request.course_id, name="course_id")
    assert_equal(response.exercise.max_score, request.max_score, name="max_score")
    assert_equal(response.exercise.min_score, request.min_score, name="min_score")
    assert_equal(response.exercise.order_index, request.order_index, name="order_index")
    assert_equal(response.exercise.description, request.description, name="description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, name="estimated_time")


@allure.step("Проверка данных задания")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные задания соответствуют ожиданиям.

    :param actual: Фактические данные задания.
    :param expected: Ожидаемые данные задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Проверка данных задания")

    assert_equal(actual.id, expected.id, name="id")
    assert_equal(actual.title, expected.title, name="title")
    assert_equal(actual.course_id, expected.course_id, name="course_id")
    assert_equal(actual.max_score, expected.max_score, name="max_score")
    assert_equal(actual.min_score, expected.min_score, name="min_score")
    assert_equal(actual.order_index, expected.order_index, name="order_index")
    assert_equal(actual.description, expected.description, name="description")
    assert_equal(actual.estimated_time, expected.estimated_time, name="estimated_time")


@allure.step("Проверка ответа на получение списка заданий")
def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_responses: list[ExerciseResponseSchema]
):
    """
    Проверяет, что ответ на получение списка заданий соответствует ответам на создание заданий.

    :param get_exercises_response: Ответ API на получение списка заданий.
    :param create_exercise_response: Список API ответов при создании заданий.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Проверка ответа на получение списка заданий")

    assert_length(actual=get_exercises_response.exercises, expected=create_exercise_responses, name="exercises")

    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(actual=get_exercises_response.exercises[index], expected=create_exercise_response.exercise)


@allure.step("Проверка ответа на получение задания")
def assert_get_exercise_response(get_exercise_response: ExerciseResponseSchema, create_exercise_response: ExerciseResponseSchema):
    """
    Проверяет, что ответ на получение данных задания соответствует ответу на создание задания.

    :param get_exercise_response: Ответ API на получение данных задания.
    :param create_exercise_response: Ответ API на создание задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Проверка ответа на получение задания")

    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)


@allure.step("Проверка ответа на обновление задания")
def assert_update_exercise_response(request: UpdateExerciseRequestSchema, response: ExerciseResponseSchema):
    """
    Проверяет, что ответ на обновление задания соответствует данным из запроса.

    :param request: Исходный запрос на обновление задания.
    :param response: Ответ API c обновленными данными задания.
    :raise AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Проверка ответа на обновление задания")

    assert_equal(response.exercise.title, request.title, name="title")
    assert_equal(response.exercise.max_score, request.max_score, name="max_score")
    assert_equal(response.exercise.min_score, request.min_score, name="min_score")
    assert_equal(response.exercise.order_index, request.order_index, name="order_index")
    assert_equal(response.exercise.description, request.description, name="description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, name="estimated_time")


@allure.step("Проверка ошибки, если задание с указанным идентификатором не найдено")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если задание с указанным exercise_id не найдено.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому "Exercise not found".
    """
    logger.info("Проверка ошибки, если задание с указанным идентификатором не найдено")

    expected = InternalErrorResponseSchema(details="Exercise not found") # Формируем текст ожидаемого ответа
    assert_internal_error_response(actual, expected) # проверяем, что фактический ответ соответствует ожидаемому

