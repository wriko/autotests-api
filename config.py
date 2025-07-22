from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, HttpUrl, FilePath


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
        env_file=".env",  # Указываем, из какого файла читать настройки
        env_file_encoding="utf-8",  # Указываем кодировку файла
        env_nested_delimiter="."  # Указываем разделитель для вложенных переменных
    )

    test_data: TestDataConfig  # настройки тестовых данных
    http_client: HTTPClientConfig # настройки http клиента


settings = Settings()
