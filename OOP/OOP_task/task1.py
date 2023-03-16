# Создайте класс, который содержит атрибуты для хранения информации о длине, ширине и высоте объекта.
# Используя property, реализуйте методы для получения и установки объема этого объекта.

class Area:
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    @property
    def volume(self):
        total = self._length * self._width * self._height
        if isinstance(total, int):
            return total
        else:
            raise TypeError("Error data value is int")

    @volume.setter
    def volume(self, val):
        if val <= 0:
            raise ValueError("Volume must be positive")
        factor = (val / self._length * self._width * self._height) ** (1 / 3)
        self._length *= factor
        self._width *= factor
        self._height *= factor


p1 = Area(2, 2, 2)
print(p1.volume)
