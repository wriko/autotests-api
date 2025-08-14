import pytest

from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
import allure
from allure_commons.types import Severity



@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)  # статическая аннотация для allure, которая задает теги для класса. Берутся из Enam AllureTag
@allure.epic(AllureEpic.LMS)  # статическая аннотация для allure, которая задает эпик для класса. Берутся из Enam AllureEpic
@allure.feature(AllureFeature.USERS)  # статическая аннотация для allure, которая задает фичу для класса. Берутся из Enam AllureFeature
@allure.parent_suite(AllureEpic.LMS)  # allure.parent_suite == allure.epic
@allure.suite(AllureFeature.USERS)  # allure.suite == allure.feature
class TestUser:
    @pytest.mark.parametrize("email", ["mail.ru", "gmail.com", "example.com"])  # параметризация теста по доменам электронной почты/ Тест test_create_user будет запущен три раза с разными значениями email: "mail.ru", "gmail.com", "example.com"
    @allure.tag(AllureTag.CREATE_ENTITY)  # статическая аннотация для allure, которая задает теги для теста. Берутся из Enam AllureTag
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Создание пользователя")  # статическая аннотация для allure, которая задает название теста
    @allure.severity(Severity.BLOCKER)  # статическая аннотация для allure, которая задает важность теста. Берутся из Enam Severity
    @allure.sub_suite(AllureStory.CREATE_ENTITY)  # allure.sub_suite == allure.story
    def test_create_user(self, email: str, public_users_client: PublicUsersClient):  # Инициализация клиента public_users_client с помощью фикстуры, которая возвращает экземпляр PublicUsersClient
        allure.dynamic.title(f"Создание пользователя c {email}")  # динамическая аннотация для allure, которая задает описание теста

        request = CreateUserRequestSchema(email=fake.email(domain=email))  # создание запроса на создание пользователя с помощью класса CreateUserRequestSchema, который наследуется от BaseModel для создания моделей данных с помощью Pydantic. Параметр email будет передан в качестве аргумента в метод email класса fake, который генерирует случайный email с указанным доменом из параметрайза.
        response = public_users_client.create_user_api(request)  # отправка запроса на создание пользователя c помощью метода create_user_api (для анализа Response)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)  # преобразование ответа в словарь с данными пользователя с помощью метода model_value_json класса CreateUserResponseSchema

        assert_status_code(response.status_code, HTTPStatus.OK)  # проверка, что статус ответа равен 200 (успешное создание пользователя)
        assert_create_user_response(request, response_data)  # проверка, что ответ соответствует запросу на создание пользователя

        validate_json_schema(response.json(), response_data.model_json_schema())  # проверка, что ответ соответствует схеме CreateUserResponseSchema


    @allure.tag(AllureTag.GET_ENTITY)  # статическая аннотация для allure, которая задает теги для теста. Берутся из Enam AllureTag
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Получение текущего пользователя")
    @allure.severity(Severity.CRITICAL)  # статическая аннотация для allure, которая задает важность теста. Берутся из Enam Severity
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_user_me(self, function_user: UserFixture, private_users_client: PrivateUsersClient):  # Инициализация клиента private_users_client с помощью фикстуры, которая возвращает экземпляр PrivateUsersClient
        response = private_users_client.get_user_me_api()  # отправка запроса на получение текущего пользователя c помощью метода get_user_me_api (для анализа Response)
        response_data = GetUserResponseSchema.model_validate_json(response.text)  # преобразование ответа в словарь с данными пользователя с помощью метода model_value_json класса CreateUserResponseSchema

        assert_status_code(response.status_code, HTTPStatus.OK)  # проверка, что статус ответа равен 200 (успешное создание пользователя)
        assert_get_user_response(response_data, function_user.response)  # проверка, что ответ соответствует запросу на создание пользователя. response_data - это ответ на получение пользователя, а function_user.response - это ответ на создание пользователя

        validate_json_schema(response.json(), response_data.model_json_schema())  # проверка, что ответ соответствует схеме GetUserResponseSchema

