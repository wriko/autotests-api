from httpx import Client, URL, QueryParams, Response
from typing import Any

from httpx._types import RequestData, RequestFiles
import allure


class APIClient:
    def __init__(self, client: Client): # тут мы принимаем экземпляр httpx.Client для выполнения HTTP-запросов и передаем его в конструктор класса ApiClient
        """
        Базовый API клиент, принимающий объект httpx.Client.

        :param client: экземпляр httpx.Client для выполнения HTTP-запросов
        """
        self.client = client # сохраняем переданный клиент в атрибуте класса для дальнейшего использования в методах класса и его потомках


    @allure.step("Делаем GET запрос к {url}")
    def get(self, url: URL | str, params: QueryParams | None = None) -> Response: # метод get принимает URL-адрес эндпоинта и параметры запроса и возвращает объект Response с данными ответа
        """
        Выполняет GET-запрос.

        :param url: URL-адрес эндпоинта.
        :param params: GET-параметры запроса (например, ?key=value).
        :return: Объект Response с данными ответа.
        """
        return self.client.get(url, params=params)


    @allure.step("Делаем POST запрос к {url}")
    def post(
            self, url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        """
        Выполняет POST-запрос.

        :param url: URL-адрес эндпоинта.
        :param json: Данные в формате JSON.
        :param data: Форматированные данные формы (например, application/x-www-form-urlencoded).
        :param files: Файлы для загрузки на сервер.
        :return: Объект Response с данными ответа.
        """
        return self.client.post(url, json=json, data=data, files=files)


    @allure.step("Делаем PATCH запрос к {url}")
    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Выполняет PATCH-запрос (частичное обновление данных).

        :param url: URL-адрес эндпоинта.
        :param json: Данные для обновления в формате JSON.
        :return: Объект Response с данными ответа.
        """
        return self.client.patch(url, json=json)


    @allure.step("Делаем DELETE запрос к {url}")
    def delete(self, url: URL | str) -> Response:
        """
        Выполняет DELETE-запрос (удаление данных).

        :param url: URL-адрес эндпоинта.
        :return: Объект Response с данными ответа.
        """
        return self.client.delete(url)
