# Напишите класс "Человек", который содержит информацию об имени, возрасте и месте жительства.
# Используйте магический метод setattr, чтобы проверять значения атрибутов и присваивать их соответствующим свойствам..

class Human:
    def __init__(self, name, age, location):
        self._name = name
        self._age = age
        self._location = location

    def __setattr__(self, key, value):
        if key == '_name' or key == '_age' or key == '_location':
            return super().__setattr__(key, value)
        else:
            self.__dict__[key] = value


p1 = Human('Ivan', 35, 'Питер')
p1._age = 25
print(p1._location)
