import pytest

# @pytest.mark.smoke
# def test_smoke_case():
#     assert 1 + 1 == 2
#
# @pytest.mark.regression
# def test_regression_case():
#     assert 2 * 2 == 4


# @pytest.mark.regression
# class TestUserAuthentication:
#     @pytest.mark.smoke
#     def test_user_login(self):
#         # Здесь будет код для теста аутентификации пользователя
#         assert True  # Замените на реальную проверку
#
#     def test_password_reset(self):
#         # Здесь будет код для теста сброса пароля
#         assert True  # Замените на реальную проверку
#
#     @pytest.mark.slow
#     def test_user_logout(self):
#         # Здесь будет код для теста выхода пользователя
#         assert True  # Замените на реальную проверку

# python -m pytest -s -v -m "regression and not slow"


# @pytest.mark.regression
# @pytest.mark.smoke
# @pytest.mark.critical
# def test_critical_function():
#     # Тест для критической функции, которая должна выполняться быстро
#     assert True  # Замените на реальную проверку

#  python -m pytest -s -v -m "critical"