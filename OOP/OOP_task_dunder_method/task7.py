# Напишите класс "Время", который содержит часы и минуты.
# Используйте магические методы, чтобы сравнивать объекты класса "Время" по времени..

class Time:

    def __init__(self, hour, minutes):
        self._hour = hour
        self._minutes = minutes
        self.total_time = (self._hour * 60) + self._minutes

    def __eq__(self, other):
        return self.total_time == other.total_time

    def __gt__(self, other):
        return self.total_time == other.total_time

    def __ge__(self, other):
        return self.total_time == other.total_time


p1 = Time(3, 100)
p2 = Time(3, 100)
print(p1 >= p2)
