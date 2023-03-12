import pytest
from OOP_task.task1 import Area


class TestArea:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def value(self):
        return self.x * self.y * self.z


def test_value():
    obj = TestArea(2, 2, 2)
    assert obj.value() == 8
