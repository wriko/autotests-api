import pytest
from _pytest.fixtures import SubRequest  # импортируем SubRequest для использования в фикстуре и параметризации


@pytest.mark.parametrize("number",[1, 2, 3, -1])  # в параметризацию передаем список чисел, которые будет применяться тестом
def test_numbers(number: int):
    assert number > 0, f"Expected {number} to be greater than 0"


@pytest.mark.parametrize("number, expected", [(1, 1),(2, 4),(3, 9)]) # в параметризацию передаем кортежи, которые будут применяться тестом
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize("os", ["Windows", "Linux", "MacOS"])
@pytest.mark.parametrize("host", ["https://dev.company.com", "https://test.company.com", "https://stage.company.com"])
def test_miltiplication_number(os: str, host: str):
    assert len(os) > 0
# tests/test_parametrization.py::test_miltiplication_number[https://dev.company.com-Windows] PASSED
# tests/test_parametrization.py::test_miltiplication_number[https://dev.company.com-Linux] PASSED
# tests/test_parametrization.py::test_miltiplication_number[https://dev.company.com-MacOS] PASSED
# tests/test_parametrization.py::test_miltiplication_number[https://test.company.com-Windows] PASSED
# tests/test_parametrization.py::test_miltiplication_number[https://test.company.com-Linux] PASSED
# tests/test_parametrization.py::test_miltiplication_number[https://test.company.com-MacOS] PASSED
# tests/test_parametrization.py::test_miltiplication_number[https://stage.company.com-Windows] PASSED
# tests/test_parametrization.py::test_miltiplication_number[https://stage.company.com-Linux] PASSED
# tests/test_parametrization.py::test_miltiplication_number[https://stage.company.com-MacOS] PASSED



# для параметризации можно использовать фикстуры, которые будут возвращать значения для параметров тестов
@pytest.fixture(params=["https://dev.company.com", "https://test.company.com", "https://stage.company.com"])
def host(request: SubRequest) -> str:
    return request.param


def test_host(host: str):
    print(f"running test with host:, {host}")
# tests/test_parametrization.py::test_host[https://dev.company.com] running test with host:, https://dev.company.com
# PASSED
# tests/test_parametrization.py::test_host[https://test.company.com] running test with host:, https://test.company.com
# PASSED
# tests/test_parametrization.py::test_host[https://stage.company.com] running test with host:, https://stage.company.com
# PASSED


# параметризация классов
@pytest.mark.parametrize("user", ["Alize", "Zara"])
class TestOperation:
    def test_user_with_operations(self, user: str):
        print(f"running test with host:, {user}")


    def test_user_without_operations(self, user: str):
        print(f"running test without host:, {user}")


# идентификаторы параметризации можно задавать с помощью метаданных

users = {
    "+7000000011": "first",
    "+7000000022": "second",
    "+7000000033": "third"
}

@pytest.mark.parametrize("phone_number", users.keys(), ids=lambda phone_number: f"{phone_number}: {users[phone_number]}")
def test_identifiers(phone_number: str):
    pass

