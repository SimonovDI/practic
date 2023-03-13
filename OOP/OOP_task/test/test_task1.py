import pytest
from OOP_task.task1 import Area

"""ожидаемое значение"""


def test_value_int():
    obj = Area(2, 2, 2)
    assert obj.val == 8


""" Проверка функции на значение int"""


def test_value_str():
    obj = Area(2, 2, 2)
    assert obj.val == int(obj.value)
