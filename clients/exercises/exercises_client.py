from httpx import Response
from clients.api_client import APIClient

from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.exercises.exercises_schema import ExerciseResponseSchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesQuerySchema, GetExercisesResponseSchema  # Импортируем необходимые схемы из exercises_schema.py



class ExercisesClient(APIClient):  # Клиент для работы с /api/v1/exercises
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:  #
        """
        Получение списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))  # Вызов метода get класса APIClient с передачей пути "/api/v1/exercises" и параметров запроса params=query. Ответ от сервера возвращается в виде объекта httpx.Response.


    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение информации о задании по exercise_id

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")


    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Создание задания.

        :param request: Словарь с данными для создания задания.
        Принимает: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", request.model_dump(by_alias=True))


    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Обновление данных задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удавление задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}") # Вызов метода delete класса APIClient с передачей пути "/api/v1/exercises/{exercise_id}" и данных запроса request. Ответ от сервера возвращается в виде объекта httpx.Response.


    # Добавляем функции для работы с данными (для более удобного использования клиента)
    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Получение списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде словаря.
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)


    def get_exercise(self, exercise_id) -> ExerciseResponseSchema:
        """
        Получение информации о задании по exercise_id

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде словаря.
        """
        response = self.get_exercise_api(exercise_id)
        return ExerciseResponseSchema.model_validate_json(response.text)


    def create_exercise(self, request: CreateExerciseRequestSchema) -> ExerciseResponseSchema:
        """
        Создание задания.

        :param request: Словарь с данными для создания задания.
        Принимает: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде словаря.
        """
        response = self.create_exercise_api(request)
        return ExerciseResponseSchema.model_validate_json(response.text)


    def update_exercise(self, exercise_id, request: UpdateExerciseRequestSchema) -> ExerciseResponseSchema:
        """
        Обновление данных задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с данными для обновления задания.
        Принимает: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде словаря.
        """
        response = self.update_exercise_api(exercise_id, request)
        return ExerciseResponseSchema.model_validate_json(response.text)


# Добавляем builder для ExercisesClient
def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создает экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :param user: Словарь с email и password для аутентификации.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))