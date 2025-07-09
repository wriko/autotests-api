from http import HTTPStatus

import pytest

from clients.errors_schema import ValidationErrorResponseSchema, InternalErrorResponseSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from fixtures.files import FileFixture
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response, assert_get_file_response, \
    assert_create_file_with_empty_filename_response, assert_create_file_with_empty_directory_response, \
    assert_file_not_found_response, assert_get_file_with_incorrect_file_id_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.files
@pytest.mark.regression
class TestFiles:
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text) # преобразование ответа в словарь с данными пользователя с помощью метода model_value_json

        assert_status_code(response.status_code, HTTPStatus.OK)  # проверка, что статус ответа равен 200 (успешное создание пользователя)
        assert_create_file_response(request, response_data)  # проверка, что ответ соответствует запросу на создание файла

        validate_json_schema(response.json(), response_data.model_json_schema())  # проверка, что ответ соответствует схеме CreateFileResponseSchema


    def test_get_file(self, files_client: FilesClient, function_file: FileFixture):
        response = files_client.get_file_api(function_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)  # проверка, что статус ответа равен 200 (успешное создание пользователя)
        assert_get_file_response(response_data, function_file.response)  # проверка, что ответ соответствует запросу на создание файла

        validate_json_schema(response.json(), response_data.model_json_schema())  # проверка, что ответ соответствует схеме CreateFileResponseSchema


    def test_create_file_with_empty_filename(self, files_client: FilesClient):
        request = CreateFileRequestSchema(filename ="", upload_file="./testdata/files/image.png")
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)  # проверка, что статус ответа равен 422
        assert_create_file_with_empty_filename_response(response_data)  # проверка, что ответ соответствует запросу на создание файла

        validate_json_schema(response.json(), response_data.model_json_schema()) # проверка, что ответ соответствует схеме CreateFileResponseSchema



    def test_create_file_with_empty_directory(self, files_client: FilesClient):
        request = CreateFileRequestSchema(directory ="", upload_file="./testdata/files/image.png")
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)  # проверка, что статус ответа равен 422
        assert_create_file_with_empty_directory_response(response_data)  # проверка, что ответ соответствует запросу на создание файла

        validate_json_schema(response.json(), response_data.model_json_schema()) #


    def test_delete_file(self, files_client: FilesClient, function_file: FileFixture):
        delete_response = files_client.delete_file_api(function_file.response.file.id)

        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = files_client.get_file_api(function_file.response.file.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_file_not_found_response(get_response_data)

        validate_json_schema(get_response.json(), get_response_data.model_json_schema())


    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient):
        # отправляем запрос на получение файла с некорректным file_id
        get_response = files_client.get_file_api(file_id="incorrect-file-id")
        # проверка, что ответ соответствует схеме ValidationErrorResponseSchema
        response_data = ValidationErrorResponseSchema.model_validate_json(get_response.text)
        # Проверка, что код ответа соответствует ожиданиям (422 - Unprocessable Entity)
        assert_status_code(get_response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)  # проверка, что статус ответа равен 422
        # Проверка, что ответ API соответствует ожидаемой валидационной ошибке
        assert_get_file_with_incorrect_file_id_response(response_data) #
        # Дополнительная проверка структуры JSON, чтобы убедиться, что схема валидационного ответа не изменилась
        validate_json_schema(get_response.json(), response_data.model_json_schema())



