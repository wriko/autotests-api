import pytest
from allure_commons.types import Severity

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from http import HTTPStatus

from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
import allure



@pytest.mark.regression
@pytest.mark.authentication
@allure.tag(AllureTag.AUTHENTICATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)  # статическая аннотация для allure, которая задает эпик для класса. Берутся из Enam AllureEpic
@allure.feature(AllureFeature.AUTHENTICATION)  # статическая аннотация для allure, которая задает фичу для класса. Берутся из Enam AllureFeature
@allure.parent_suite(AllureEpic.LMS)  # allure.parent_suite == allure.epic
@allure.suite(AllureFeature.AUTHENTICATION)  # allure.suite == allure.feature
class TestAuthentication:
    @allure.story(AllureStory.LOGIN)  # статическая аннотация для allure, которая задает историю для метода. Берутся из Enam AllureStory
    @allure.title('Тест аутентификации пользователя c корректным логином и паролем')
    @allure.severity(Severity.BLOCKER)  # статическая аннотация для allure, которая задает важность теста. Берутся из Enam Severity
    @allure.sub_suite(AllureStory.LOGIN)
    def test_login(self, function_user: UserFixture, authentication_client: AuthenticationClient):  # инициализация клиента и создание пользователя с помощью фикстуры function_user, которая возвращает экземпляр UserFixture с данными пользователя
        # подготовка данных для аутентификации
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)  # создание запроса на аутентификацию с помощью LoginRequestSchema, используя email и password из фикстуры function_user
        # отправка запроса на аутентификацию c помощью метода login_api и данных запроса login_request
        response = authentication_client.login_api(request)

        # десериализация JSON-ответа в LoginResponseSchema
        response_data = LoginResponseSchema.model_validate_json(response.text)

        # проверки ответа на аутентификацию
        assert_status_code(response.status_code, HTTPStatus.OK)  # проверка, что статус-код ответа соответствует ожидаемому (200 OK)
        assert_login_response(response_data)  # проверка, что ответ соответствует ожидаемому формату
        validate_json_schema(response.json(), response_data.model_json_schema())  # проверка, что ответ соответствует схеме LoginResponseSchema