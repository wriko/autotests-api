import pytest

@pytest.mark.xfail(reason="Найден баг в приложении, из-за которого тест падает с ошибкой")
def test_with_bug():
    assert 1 ==2

@pytest.mark.xfail(reason="Баг уже исправлен, но на тесте осталась маркировка xfail")
def test_without_bug():
    ...

@pytest.mark.xfail(reason="внешний сервис недоступен")

def test_external_service_is_unavailable():
    assert 1 ==2


#> python -m pytest -s -v -k "test_with_bug or test_without_bug or test_external_service_is_unavailable"

# tests/test_pytest_xfail.py::test_with_bug XFAIL (Найден баг в приложении, из-за которого тест падает с ошибкой)
# tests/test_pytest_xfail.py::test_without_bug XPASS (Баг уже исправлен, но на тесте осталась маркировка xfail)
# tests/test_pytest_xfail.py::test_external_service_is_unavailable XFAIL (внешний сервис недоступен)

