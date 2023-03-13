import pytest

from OOP_task.task2 import Account

"""Проверяем Имя на строковое значение"""


def test_hash_func():
    obj = Account('Ivan', 123456)
    assert obj.hash_func != str
