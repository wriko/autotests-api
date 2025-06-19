from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict


class GetExercisesQueryDict(TypedDict): # Тип словаря с данными для получения списка заданий для определенного курса. Принимает: courseId (идентификатор курса dля которого необходимо получить список заданий).
    """
    Описание структуры запроса на получение списка заданий для определенного курса.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict): # Тип словаря с данными для создания задания. Принимает: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):  # Клиент для работы с /api/v1/exercises
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:  #
        """
        Получение списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query) # Вызов метода get класса APIClient с передачей пути "/api/v1/exercises" и параметров запроса params=query. Ответ от сервера возвращается в виде объекта httpx.Response.

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение информации о задании по exercise_id

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")  # Вызов метода get класса APIClient с передачей пути "/api/v1/exercises/{exercise_id}" и параметров запроса params=query. Ответ от сервера возвращается в виде объекта httpx.Response.

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создание задания.

        :param request: Словарь с данными для создания задания.
        Принимает: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", request)  # Вызов метода post класса APIClient с передачей пути "/api/v1/exercises" и данных запроса request. Ответ от сервера возвращается в виде объекта httpx.Response.

    def update_exercise_api(self, exercise_id: str) -> Response:
        """
        Обновление данных задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}") # Вызов метода patch класса APIClient с передачей пути "/api/v1/exercises/{exercise_id}" и данных запроса request. Ответ от сервера возвращается в виде объекта httpx.Response.

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удавление задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}") # Вызов метода delete класса APIClient с передачей пути "/api/v1/exercises/{exercise_id}" и данных запроса request. Ответ от сервера возвращается в виде объекта httpx.Response.
