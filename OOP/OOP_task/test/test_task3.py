import pytest
from OOP_task.task3 import Shopping_list


class ShoppingListTest:
    """проверка количества значений в списке"""
    def __init__(self, spisok):
        self.spisok = spisok

    def lst(self):
        return len(self.spisok)


def test_lst():
    obj = ShoppingListTest(['яблоко', 'груша', 'банан'])
    assert obj.lst() > 0
