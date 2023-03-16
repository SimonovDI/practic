import pytest

from OOP.OOP_task.task1 import Area



"""ожидаемое значение"""


def test_value_int():
    obj = Area(2, 2, 2)
    assert obj.volume == 8


""" Проверка функции на значение int"""


def test_value_str():
    obj = Area(2, 2, 2)
    assert isinstance(obj.volume, int)
