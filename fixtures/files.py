import pytest
from pydantic import BaseModel
from fixtures.users import UserFixture
from clients.files.files_client import FilesClient, get_files_client
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema


class FileFixture(BaseModel):
    request: CreateFileRequestSchema # данные запроса на загрузку файла
    response: CreateFileResponseSchema # ответ от API после успешного создания файл


# Фикстура создает клиент FilesClient, который будет использоваться для работы с API загрузки файлов.
@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient: # В аргумент передается function_user — пользователь, полученный через фикстуру UserFixture. Используется метод get_files_client, который создает клиент, уже настроенный для работы от имени данного пользователя.
    return get_files_client(function_user.authentication_user) #Фикстура возвращает объект FilesClient, который можно использовать в тестах.

# Фикстура автоматически создает тестовый файл перед каждым тестом и возвращает информацию о нем
@pytest.fixture
def function_file(files_client: FilesClient) -> FileFixture:
    request = CreateFileRequestSchema(upload_file="./testdata/files/image.png") # Создается объект request типа CreateFileRequestSchema, в котором указывается путь к тестовому файлу (./testdata/files/image.png).
    response = files_client.create_file(request) # Затем files_client.create_file(request) отправляет запрос в API, загружая файл.
    return FileFixture(request=request, response=response) # После успешного создания файла возвращается объект FileFixture, содержащий данные запроса и ответа API.
