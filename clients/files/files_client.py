from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

class File(TypedDict):
    """
    Описание структуры файла.
    """
    id: str
    filename: str
    directory: str
    url: str


class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseDict(TypedDict):
    """
    Описание структуры ответа создание файла.
    """
    file: File

class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/files",
            data= request,
            files={"upload_file": open(request["upload_file"], "rb")}
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")  # удаление файла по идентификатору. Возвращает 204. Необходимо проверить, что файл действительно удален. В случае удаления возвращает пустой объект.

    # Добавили новый метод
    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict: # Метод создания файла с использованием клиента FilesClient. Возвращает ответ от сервера. Обязательно проверить, что файл действительно создан.
        response = self.create_file_api(request)
        return response.json()


 # Добавляем builder для FilesClient
def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))  # Настройка клиента с базовым URL и таймаутом