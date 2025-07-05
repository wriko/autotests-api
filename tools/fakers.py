from faker import Faker


class Fake:
    """
    Класс для генерации случайных данных с использованием библиотеки Faker.
    """

    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker для генерации случайных данных.
        """
        self.faker = faker

    def text(self) -> str:
        """
        Генерирует случайный текст.

        :return: Случайный текст.
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Генерирует случайный UUID4.

        :return: Случайный UUID4.
        """
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        Генерирует случайный email.

        :param domain: Домен электронной почты (например, "example.com").
        Если не указан, будет использован случайный домен.
        :return: Случайный email.
        """
        return self.faker.email(domain=domain)

    def sentence(self) -> str:
        """
        Генерирует случайное предложение.

        :return: Случайное предложение.
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Генерирует случайный пароль.

        :return: Случайный пароль.
        """
        return self.faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)

    def last_name(self) -> str:
        """
        Генерирует случайную фамилию.

        :return: Случайная фамилия.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Генерирует случайное имя.

        :return: Случайное имя.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Генерирует случайное отчество.

        :return: Случайное отчество.
        """
        return self.faker.first_name()

    def estimated_time(self) -> str:
        """
        Генерирует случайное время в формате 'X weeks'.

        :return: Случайное время в формате 'X weeks'.
        """
        return f"{self.integer(1,100)} weeks"

    def integer(self, min_value: int = 0, max_value: int = 100) -> int:
        """
        Генерирует случайное целое число в диапазоне 0-100.

        :param min_value: Минимальное значение (включительно).
        :param max_value: Максимальное значение (включительно).
        :return: Случайное целое число.
        """
        return self.faker.random_int(min=min_value, max=max_value)

    def max_score(self) -> int:
        """
        Генерирует случайный максимальный балл в диапазоне 50-100.

        :param min_value: Минимальное значение (включительно).
        :param max_value: Максимальное значение (включительно).
        :return: Случайный максимальный балл.
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Генерирует случайный минимальный балл в диапазоне 1-49.

        :param min_value: Минимальное значение (включительно).
        :param max_value: Максимальное значение (включительно).
        :return: Случайный минимальный балл.
        """
        return self.integer(1, 49)


# Создаем экземпляр класса Fake с использованием Faker
fake = Fake(faker = Faker())  # Создание экземпляра класса `Fake` с использованием локали по умолчанию для генерации случайных данных на английском языке.

fake_ru = Fake(faker = Faker('ru-RU'))  # Cоздание экземпляра класса `Fake` с указанием локали 'ru-RU' для генерации случайных данных на русском языке.
