import random
import pytest

PLATFORM = 'linux'

@pytest.mark.flaky(reruns=3, reruns_delay=2) # если тест упадет, он будет перезапущен до 3 раз с задержкой в 2 секунды между попытками
def test_rerun():
    assert random.choice([True, False])

# tests/test_rerun.py::test_rerun RERUN
# tests/test_rerun.py::test_rerun RERUN
# tests/test_rerun.py::test_rerun RERUN
# tests/test_rerun.py::test_rerun PASSED


@pytest.mark.flaky(reruns=3, reruns_delay=2) # если каждый тест в классе упадет, он будет перезапущен до 3 раз с задержкой в 2 секунды между попытками
class TestReruns:
    def test_rerun_1(self):
        assert random.choice([True, False])

    def test_rerun_2(self):
        assert random.choice([True, False])


# перезапуски с условиями
@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == 'linux') # если тест упадет, он будет перезапущен до 3 раз с задержкой в 2 секунды между попытками, но только если условие PLATFORM == 'linux' выполнено
def test_rerun_with_condition():
    assert random.choice([True, False])
