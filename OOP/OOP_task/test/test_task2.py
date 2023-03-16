import pytest

from OOP.OOP_task.task2 import Account

"""Возвращается hash """


def test_hash_password():
    obj = Account('Ivan', "querty")
    assert obj.hash_password == hash("querty")





