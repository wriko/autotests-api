from clients.exercises.exercises_schema import CreateExerciseRequestSchema, ExerciseResponseSchema
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
