from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.courses.courses_schema import GetCoursesQuerySchema, CreateCourseRequestSchema, CreateCourseResponseSchema, UpdateCourseRequestSchema
import allure

class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    @allure.step("Получение списка курсов")
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/courses", params=query.model_dump(by_alias=True)) # Используем by_alias для использования алиасов ключей


    @allure.step("Получение курса по идентификатору {course_id}")
    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса по идентификатору.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")


    @allure.step("Создание курса")
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/courses", json=request.model_dump(by_alias=True)) # Отправляем POST-запрос на создание курса с данными из словаря request, преобразованного в JSON с помощью метода model_dump класса CreateCourseRequestSchema


    @allure.step("Обновление курса по идентификатору {course_id}")
    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True)) # Отправляем PATCH-запрос на обновление курса с данными из словаря request, преобразованного в JSON с помощью метода model_dump класса UpdateCourseRequestSchema


    @allure.step("Удаление курса по идентификатору {course_id}")
    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")


    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request) # Вызываем метод create_course_api для отправки запроса на создание курса и получения ответа от сервера
        return CreateCourseResponseSchema.model_validate_json(response.text)  # Преобразуем ответ в словарь с данными курса с помощью метода model_validate_json класса CreateCourseResponseSchema


# Добавляем builder для CoursesClient
def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создает экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :param user: Словарь с email и password для аутентификации.
    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))  # Настройка клиента с базовым URL и таймаутом