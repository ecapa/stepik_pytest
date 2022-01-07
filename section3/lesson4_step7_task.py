import pytest


@pytest.fixture(scope="class")  # область покрытия class означает, что фикстура будет вызываться один раз для класса
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)  # параметр autouse=True указывает на то, что фикстура будет запускаться для каждого теста, даже без вызова
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass

    def test_second_smiling_faces(self, prepare_faces):
        pass

# У нас есть набор тестов, который использует несколько фикстур.
# Посчитайте, сколько смайликов будет напечатано при выполнении этого тестового класса?
# pytest -s test_fixture7.py
