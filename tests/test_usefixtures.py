import pytest


@pytest.fixture
def clear_books_database():
    print("Clearing the database...")

@pytest.fixture
def fill_books_database():
    print("Filling the database...")

@pytest.mark.usefixtures("clear_books_database", "fill_books_database") # Используем фикстуры для очистки и заполнения базы данных книг  для каждого теста в классе
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...

