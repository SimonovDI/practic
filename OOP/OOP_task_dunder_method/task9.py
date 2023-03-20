# Напишите класс "Студент", который содержит имя и средний балл студента.
# Используйте магические методы для сравнения объектов класса "Студент" по их среднему баллу..

class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade
        self.gpa = (sum(grade) / len(grade))

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __gt__(self, other):
        return self.gpa > other.gpa

    def __ge__(self, other):
        return self.gpa >= other.gpa


p1 = Student('Ivanov', [4, 4, 3, 5])
p2 = Student('Petrov', [5, 5, 4, 3])
print(p1 > p2)
