import pytest

from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient


@pytest.fixture # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def authentication_client() -> AuthenticationClient:  # Аннотируем возвращаемое фикстурой значение
    return get_authentication_client() # Создаем новый API клиент для работы с аутентификацией