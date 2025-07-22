from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
import allure

class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """

    @allure.step("Получение файла по id {file_id}")
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    @allure.step("Создание файла")
    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/files",
            data= request.model_dump(by_alias=True, exclude={"upload_file"}), # model_dump преобразует объект в словарь с учетом псевдонимов полей (например, filename -> name) и исключением поля upload_file, так как оно не должно быть передано в теле запроса.
            files = {"upload_file": request.upload_file.read_bytes()}
        )

    @allure.step("Удаление файла по id {file_id}")
    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")  # удаление файла по идентификатору. Возвращает 204. Необходимо проверить, что файл действительно удален. В случае удаления возвращает пустой объект.


    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:  # Создание файла на сервере с проверкой на ошибки сервера и получением ответа сервера
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text) # Преобразование ответа в словарь с данными файла с помощью метода model_value_json класса CreateFileResponseSchema из файлов_schema.py и запись его в переменную response.


 # Добавляем builder для FilesClient
def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))  # Настройка клиента с базовым URL и таймаутом