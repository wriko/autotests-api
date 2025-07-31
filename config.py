from typing import Self

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath


class HTTPClientConfig(BaseModel):  # настройки http клиента
    url: HttpUrl  # урл
    timeout: float  # таймаут

    @property
    def client_url(self) -> str:  # перевод урла в строку
        return str(self.url)


class TestDataConfig(BaseModel):  # настройки тестовых данных
    image_png_file: FilePath  # путь к файлу с изображением


class Settings(BaseSettings):  # настройки
    model_config = SettingsConfigDict(  # используем для переопределения настроек
        extra="allow", # разрешаем дополнительные поля в файле настроек (если они есть)
        env_file=".env",  # Указываем, из какого файла читать настройки
        env_file_encoding="utf-8",  # Указываем кодировку файла
        env_nested_delimiter="."  # Указываем разделитель для вложенных переменных
    )

    test_data: TestDataConfig  # настройки тестовых данных
    http_client: HTTPClientConfig # настройки http клиента
    allure_results_dir: DirectoryPath

    @classmethod
    def initialize(cls) -> Self: # Возвращает экземпляр класса Settings
        allure_results_dir = DirectoryPath("./allure-results")  # Создаем объект пути к папке
        allure_results_dir.mkdir(exist_ok=True)  # Создаем папку allure-results, если она не существует

        return Settings(allure_results_dir=allure_results_dir) # Передаем allure_results_dir в инициализацию настроек

# Теперь вызываем метод initialize
settings = Settings.initialize()
