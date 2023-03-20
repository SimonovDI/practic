# Напишите класс "Студент", который содержит имя и номер студенческого билета.
# Используйте магический метод hash, чтобы создать уникальный идентификатор для каждого объекта класса "Студент".
# Проверьте что экземпляры класса можно использовать как ключи в словаре..

class Student:

    def __init__(self, name, number_stud):
        self._name = name
        self._number_stud = number_stud

    def __hash__(self):
        return hash((self._name, self._number_stud))

    def check_instance(self):
        if isinstance((self._name and self._number_stud), (int, float, tuple, str, frozenset)):
            return hash((self._name, self._number_stud))
        raise TypeError('Error data')


p1 = Student('Ivan', 123)
print(hash(p1))
p1.check_instance()
