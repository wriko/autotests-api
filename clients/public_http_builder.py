from httpx import Client


def get_public_http_client() -> Client:
    """
    Функция создает экземпляр объекта httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(base_url='http://localhost:8000', timeout=100)  # Настройка клиента с базовым URL и таймаутом