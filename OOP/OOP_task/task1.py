# Создайте класс, который содержит атрибуты для хранения информации о длине, ширине и высоте объекта.
# Используя property, реализуйте методы для получения и установки объема этого объекта.
class Area:
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    @property
    def obj(self):
        return self._length * self._width * self._height

    @obj.setter
    def obj(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height


p1 = Area(5, 5, 5)
p1._height = 15
print(p1.__dict__)
