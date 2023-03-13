# Создайте класс "Сотрудник", который будет содержать атрибуты экземпляра "имя", "должность" и "зарплата".
# Используйте инкапсуляцию, чтобы скрыть данные о зарплате и обеспечить доступ к ним только через методы класса.

# class Emp:
#
#     def __init__(self, name, pos, zp):
#         self._name = name
#         self._pos = pos
#         self._zp = zp * 1000
#
#     def salary(self):
#         return self._zp
#
#     def info(self):
#         return f'{self._name}:{self._pos}--{self._zp}'
#
#
# s1 = Emp('Иван', 'программист', 250)
# print(s1.salary())
# print(s1.info())


# Создайте класс "Животное", который будет содержать методы "питание" и "движение".
# Напишите классы "Собака" и "Кошка", которые наследуют класс "Животное" и реализуют свои методы для питания и движения.

# class Animal:
#     def __init__(self, food, move):
#         self._food = food
#         self._move = move
#
#     def animal_food(self):
#         return self._food
#
#     def animal_move(self):
#         return self._move
#
#
# class Dog(Animal):
#     def __init__(self, food, move):
#         super().__init__(food, move)
#         self._food = food
#         self._move = move
#
#     def dog_food(self):
#         return self._food * 2
#
#     def dog_move(self):
#         return (self._move * 10) + 5
#
#
# class Cat(Animal):
#     def __init__(self, food, move):
#         super().__init__(food, move)
#         self._food = food
#         self._move = move
#
#     def cat_food(self):
#         return self._food * 5
#
#     def cat_move(self):
#         return self._move + 100


# Напишите класс, в котором должна быть функция max_element, которая находит максимальный элемент в списке.
# Функция должна работать для списков любого типа, который поддерживает оператор сравнения. Например:
# my_class.max_element([1, 2, 3])    # 3
# my_class.max_element(['a', 'b', 'c'])   # 'c'
# class MyClass:
#     def __init__(self, lst):
#         self._lst = lst
#
#     def max_element(self):
#         return max(self._lst)
#
#
# s1 = MyClass({1, 2, 3})
# s2 = MyClass(['a', 'b', 'c'])
# print(s1.__dict__)
# print(s2.max_element())

# 1. Создайте контекстный менеджер, который будет выводить время, затраченное на выполнение блока кода.
# 1 вариант
# import time
# from contextlib import contextmanager


# @contextmanager
# def decorat():
#     start = time.time()
#     yield
#     end = time.time() - start
#     print(end)
#
#
# with decorat():
#         lst = []
#         for i in range(1, 1000000):
#             lst.append(i)


# 2й способ
# class Times:
#     lst = []
#
#     def __init__(self, a=int):
#         self._a = a
#
#     def __enter__(self):
#         self.start = time.time()
#         for i in range(self._a):
#             self.lst.append(i)
#         self.end = time.time() - self.start
#         return self.end
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("финиш")
#
#
# with Times(10000) as f:
#     print(f)

# Создайте контекстный менеджер, который будет открывать и закрывать файлы автоматически. (аналог функции open)

# class fileopen:
#     def __init__(self, name, method):
#         self._name = open(name, method)
#
#     def __enter__(self):
#         return self._name
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Файл закрыт')
#         self._name.close()
#
#
# with fileopen('text.txt', 'r') as f:
#     print(f"Файл {f} открыт")

# from contextlib import contextmanager
#
#
# @contextmanager
# def openfile(name):
#     print("Файл открыт")
#     func = open(name, 'r')
#     yield func
#     print("Файл закрыт")
#
#
# with openfile("text.txt") as f:
#     data=f.read()
#     print(data)