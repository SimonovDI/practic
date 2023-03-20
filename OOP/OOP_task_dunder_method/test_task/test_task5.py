import pytest
from OOP.OOP_task_dunder_method.task5 import Queue

"Test task5"


def test_class_queue():
    obj = Queue([1, 2, 3])
    assert type(obj.__len__()) == int
    assert len(obj) == 3
