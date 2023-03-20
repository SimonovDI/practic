import pytest
from OOP.OOP_task_dunder_method.task9 import Student

""" test task9"""


def test_class_student():
    obj1 = Student('Sidorov', [4, 4, 3, 5])
    obj2 = Student('Petrov', [-4, -4, -3, 5])
    assert obj1.gpa >= 0
    assert obj2.gpa >= 0
