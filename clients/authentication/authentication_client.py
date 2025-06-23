from clients.api_client import APIClient   #  импортируем базовый класс ApiClient для выполнения HTTP-запросов
from httpx import Response  # импортируем класс Response из библиотеки httpx для работы с ответами на HTTP-запросы
from clients.public_http_builder import get_public_http_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema,  RefreshRequestSchema  # импортируем схемы для валидации данных запросов и ответов из authentication_shema.py


class AuthenticationClient(APIClient): # создаем класс AuthenticationClient, который наследуется от ApiClient для выполнения запросов к API авторизации
    """
    Клиент для работы с /api/v1/authentication
    """

    def login_api(self, request: LoginRequestSchema) -> Response: # создаем метод для отправки запроса на авторизацию
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/authentication/login', json = request.model_dump(by_alias=True)) # отправляем POST-запрос на URL /api/v1/authentication/login с данными запроса в формате JSON. Используем метод model_dump из Pydantic для преобразования схемы запроса в словарь с учетом псевдонимов полей (by_alias=True).


    def refresh_api(self, request: RefreshRequestSchema) -> Response: # создаем метод для отправки запроса на обновление токена
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/authentication/refresh', json = request.model_dump(by_alias=True))


    def login(self, request: LoginRequestSchema) -> LoginResponseSchema: # создаем метод для отправки запроса на авторизацию и получения токена авторизации
        """
        Метод выполняет аутентификацию пользователя и возвращает токен авторизации.
        """
        response = self.login_api(request) # вызываем метод для отправки запросана авторизацию и получаем ответ
        return LoginResponseSchema.model_validate_json(response.text) # преобразуем ответ в объект LoginResponseSchema с помощью метода model_validate_json из Pydantic


# Добавляем builder для AuthenticationClient
def get_authentication_client() -> AuthenticationClient:
    """
    Функция создает экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: AuthenticationClient.
    """
    return AuthenticationClient(client = get_public_http_client())  # Настройка клиента с базовым URL и таймаутом
