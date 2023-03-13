import pytest
from OOP_task.task3 import Shopping_list


def test_get_lst_count():
    obj = Shopping_list(['яблоко', 'груша', 'банан'])
    assert obj.get_lst_count > 0



