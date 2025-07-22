import pydantic
from pydantic import BaseModel, HttpUrl, Field
from tools.fakers import fake


class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str
    url: HttpUrl # URL файла (используем HttpUrl для валидации URL)
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")  # Имя файла, по умолчанию генерируется UUID с расширением .png
    directory: str = Field(default="tests")  # Директория, в которой хранится файл, по умолчанию "tests"


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")  # Имя файла, по умолчанию генерируется UUID с расширением .png
    directory: str = Field(default="tests")  # Директория, в которой хранится файл, по умолчанию "tests"
    upload_file: pydantic.FilePath


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создание файла.
    """
    file: FileSchema


class GetFileResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос файла.
    """
    file: FileSchema