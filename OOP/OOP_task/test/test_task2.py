import pytest

from OOP_task.task2 import Account


class TestAccount:
    """Проверяем пароль на числовое значение, name - на длину строки"""

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def data_name(self):
        return len(self.name)

    def data_password(self):
        return type(self.password)


def testAccount():
    obj = TestAccount("Ivan", 123456)
    assert obj.data_name() == 4
    assert obj.data_password() == int
