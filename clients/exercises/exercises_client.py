from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class Exercise(TypedDict):
    """
    Описание структуры задания.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict): # Тип словаря с данными для получения списка заданий для определенного курса. Принимает: courseId (идентификатор курса для которого необходимо получить список заданий).
    """
    Описание структуры запроса на получение списка заданий для определенного курса.
    """
    courseId: str


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на получение списка заданий для определенного курса.
    """
    exercises: list[Exercise]


class ExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на получение информации о задании по exercise_id.
    """
    exercises: Exercise


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


class UpdateExerciseRequestDict(TypedDict): # Тип словаря с данными для обновления задания. Принимает: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


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


    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Обновление данных задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", request) # Вызов метода patch класса APIClient с передачей пути "/api/v1/exercises/{exercise_id}" и данных запроса request. Ответ от сервера возвращается в виде объекта httpx.Response.


    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удавление задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}") # Вызов метода delete класса APIClient с передачей пути "/api/v1/exercises/{exercise_id}" и данных запроса request. Ответ от сервера возвращается в виде объекта httpx.Response.


    # Добавляем функции для работы с данными (для более удобного использования клиента)
    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Получение списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде словаря.
        """
        response = self.get_exercises_api(query)
        return response.json()


    def get_exercise(self, exercise_id) -> ExerciseResponseDict:
        """
        Получение информации о задании по exercise_id

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде словаря.
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()


    def create_exercise(self, request: CreateExerciseRequestDict) -> ExerciseResponseDict:
        """
        Создание задания.

        :param request: Словарь с данными для создания задания.
        Принимает: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде словаря.
        """
        response = self.create_exercise_api(request)
        return response.json()


    def update_exercise(self, exercise_id, request: UpdateExerciseRequestDict) -> ExerciseResponseDict:
        """
        Обновление данных задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с данными для обновления задания.
        Принимает: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде словаря.
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


# Добавляем builder для ExercisesClient
def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создает экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :param user: Словарь с email и password для аутентификации.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))