# Напишите класс "Фрукт", который содержит название и вес фрукта.
# Используйте магические методы, чтобы сравнивать фрукты по их весу.
class Fruit:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def __eq__(self, other):
        return self._weight == other._weight

    def __ge__(self, other):
        return self._weight == other._weight


p1 = Fruit('Ананас', 3)
p2 = Fruit('Яблоки', 3)
print(p1 == p2)