import pytest


# @pytest.fixture(autouse=True)  # Запускается каждый раз при запуске теста (автоиспользование) для всех тестов
# def analitics_data():
#     print("[AUTOUSE] Отправляем данные в сервис аналитики")


@pytest.fixture(scope="session")  # Запускается один раз на весь проект
def setting():
    print("[SESSION] Инициализируем настройки автотестов")


@pytest.fixture(scope="class")  # Запускается один раз на каждый тестовый класс
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")


@pytest.fixture(scope="function")  # Запускается каждый раз при запуске теста
def users_client():
    print("[FUNCTION] Создаем API клиент на каждый автотест")


class TestUserFlow:
    def test_user_can_login(self, setting, user, users_client):
        ...

    def test_user_can_create_course(self, setting, user, users_client):
        ...


class TestAccountFlow:
    def test_user_account(self, setting, user, users_client):
        ...


@pytest.fixture
def user_data() -> dict:
    print("Создаем пользователя до теста")  # Запускается каждый раз перед тестом
    yield {"username": "user", "email": "test@example.com"} # выполняется сам тест
    print("Удаляем пользователя после  теста")  # Запускается после теста

def test_user_email(user_data: dict):
    print(user_data)
    assert user_data["email"] == "test@example.com"

def test_user_username(user_data: dict):
    print(user_data)
    assert user_data["username"] == "user"