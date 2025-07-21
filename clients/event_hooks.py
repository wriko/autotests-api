import allure
from httpx import Request

from tools.http.curl import make_curl_from_request


def curl_event_hook(request: Request):
    """
    Event hook для автоматического прикрепления cURL команды к отчету Allure.

    :param request: HTTP-запрос, переданный в 'httpx' клиент.
    """
    curl_command = make_curl_from_request(request)

    allure.attach(curl_command, name="cURL command", attachment_type=allure.attachment_type.TEXT)