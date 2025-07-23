import allure
from httpx import Request, Response

from tools.http.curl import make_curl_from_request
from tools.logger import get_logger




logger = get_logger("HTTP_LOGGER")



def curl_event_hook(request: Request):
    """
    Event hook для автоматического прикрепления cURL команды к отчету Allure.

    :param request: HTTP-запрос, переданный в 'httpx' клиент.
    """
    curl_command = make_curl_from_request(request)

    allure.attach(curl_command, name="cURL command", attachment_type=allure.attachment_type.TEXT)


def log_request_event_hook(request: Request):
    """
    Event hook для логирования HTTP-запросов.

    :param request: HTTP-запрос, переданный в 'httpx' клиент.
    """
    logger.info(f"Выполняем {request.method} запрос к {request.url}")


def log_response_event_hook(response: Response):
    """
    Event hook для логирования HTTP-ответов.

    :param response: HTTP-ответ.
    """
    logger.info(f"Получен ответ {response.status_code} {response.reason_phrase} от {response.url}")