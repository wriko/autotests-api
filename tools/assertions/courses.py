from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CourseSchema, \
    GetCoursesResponseSchema, CreateCourseResponseSchema, CreateCourseRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user
import allure
from tools.logger import get_logger



logger = get_logger("COURSES_ASSERTIONS")



@allure.step("Проверка ответа на обновление курса")
def assert_update_course_response(request: UpdateCourseRequestSchema, response: UpdateCourseResponseSchema):
    """
    Проверяет, что ответ на обновление курса соответствует данным из запроса.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API c обновленными данными курса.
    :raise AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Проверка ответа на обновление курса")

    assert_equal(response.course.title, request.title, name="title")
    assert_equal(response.course.max_score, request.max_score, name="max_score")
    assert_equal(response.course.min_score, request.min_score, name="min_score")
    assert_equal(response.course.description, request.description, name="description")
    assert_equal(response.course.estimated_time, request.estimated_time, name="estimated_time")


@allure.step("Проверка данных курса")
def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Проверяет, что фактические данные курса соответствуют ожидаемым.

    :param actual: Фактические данные курса.
    :param expected: Ожидаемые данные курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Проверка данных курса")

    assert_equal(actual.id, expected.id, name="id")
    assert_equal(actual.title, expected.title, name="title")
    assert_equal(actual.max_score, expected.max_score, name="max_score")
    assert_equal(actual.min_score, expected.min_score, name="min_score")
    assert_equal(actual.description, expected.description, name="description")
    assert_equal(actual.estimated_time, expected.estimated_time, name="estimated_time")

    assert_file(actual.preview_file, expected.preview_file) # переиспользуем проверку на файл
    assert_user(actual.created_by_user, expected.created_by_user) # переиспользуем проверку на пользователя


@allure.step("Проверка ответа на получение списка курсов")
def assert_get_courses_response(

        get_courses_response: GetCoursesResponseSchema, #
        create_course_responses: list[CreateCourseResponseSchema]
):
    """
    Проверяет, что ответ на получение списка курсов соответствует ответам на их создание.

    :param get_courses_response: Ответ API при запросе списка курсов.
    :param create_course_responses: Список API ответов при создании курсов.
    :raises AssertionError: Если данные пользователя не совпадают.
    """
    logger.info("Проверка ответа на получение списка курсов")

    assert_length(actual=get_courses_response.courses, expected=create_course_responses, name="courses")

    for index, create_course_response in enumerate(create_course_responses):
        assert_course(actual=get_courses_response.courses[index], expected=create_course_response.course)


@allure.step("Проверка ответа на создание курса")
def assert_create_course_response(request: CreateCourseRequestSchema, response: CreateCourseResponseSchema):
    """
    Проверяет, что ответ на создание курса соответствует данным из запроса.

    :param request: Исходный запрос на создание курса.
    :param response: Ответ API c данными созданного курса.
    :raise AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Проверка ответа на создание курса")

    assert_equal(response.course.title, request.title, name="title")
    assert_equal(response.course.max_score, request.max_score, name="max_score")
    assert_equal(response.course.min_score, request.min_score, name="min_score")
    assert_equal(response.course.preview_file.id, request.preview_file_id, name="preview_file_id") # проверяем id файла в ответе соответствуют переданным данным.
    assert_equal(response.course.description, request.description, name="description")
    assert_equal(response.course.estimated_time, request.estimated_time, name="estimated_time")
    assert_equal(response.course.created_by_user.id, request.created_by_user_id, name="created_by_user_id") # проверяем id пользователя в ответе соответствуют переданным данным.


