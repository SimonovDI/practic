# Напишите класс "Стек", который содержит список элементов.
# Используйте магический метод bool, чтобы определить, является ли стек пустым или нет.

class Stack:
    def __init__(self, data):
        self._data = data

    def __bool__(self):
        return len(self._data) > 0


p1 = Stack([])
print(bool(p1))
