def test_first_try():
    print("First try")


def test_assert_positive_case():
    assert (2 + 2) == 4


def test_assert_negative_case():
    x, y = 10, 5
    assert (y + y ) == x, "Ошибка в вычислении: y + y != x"
