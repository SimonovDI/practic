# Задача 1
# Вводится, одно натуральное число — требуемый размер таблицы
# Пример 1
# Ввод: 3
# Вывод
# 1 2 3
# 2 4 6
# 3 6 9
#
# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i*j, end=' ')
#     print()


# *****************************************************************************
# Формат ввода
# Вводится одно натуральное число — требуемый размер таблицы.
# Формат вывода
# Таблица умножения заданного размера.
# Ввод
# 5
# Вывод
# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15
# 4  8 12 16 20
# 5 10 15 20 25
#
# отличие от первой задачи в том, что надо добавить отступы, чтобы таблица была ровная

# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         a = len(str(i*j))
#         if a >= 2:
#             print(f"{i*j:<1d}",end=' ')
#         else:
#             print(f"{i*j:>2d}",end=' ')
#     print()

# *******************************************************************************************************
# Задача 3
# Формат ввода
# В первой строке записано число NN — высота числового прямоугольника.
# Во второй строке указано число MM — ширина числового прямоугольника.
# 
# Формат вывода
# Нужно вывести сформированную числовую змейку требуемого размера.
# Чтобы прямоугольник был красивым, каждый его столбец следует сделать одинаковой ширины.
# 
# Пример 1
# Ввод
# 2
# 3
# Вывод
# 1 2 3
# 6 5 4
# Пример 2
# Ввод
# 4
# 6
# Вывод
#  1  2  3  4  5  6
# 12 11 10  9  8  7
# 13 14 15 16 17 18
# 24 23 22 21 20 19

# m = int(input()) # строка
# n = int(input()) # столбец
# a = 0            # счетчик
# lst = []
# for i in range(1,m+1):
#     for j in range(1,n+1):
#         a += 1
#         lst.append(a)
#     if i % 2 ==0:
#         b = reversed(lst)
#         for z in b:
#             ln = len(str(z))
#             if ln >= 1:
#                 print(f"{z:>2d}",end=' ')
#             else:
#                 print(f"{z:>1d}",end=' ')
#     if i % 2 ==1:
#         for z in lst:
#             print(f"{z:>2d}",end= ' ')
#     lst = []
#     print()
#
#
# Правильный вариант!
# m = int(input()) # строка
# n = int(input()) # столбец
# a = 0            # счетчик
# lst = []
# ln = len(str(m*n))
# for i in range(1,m+1):
#     for j in range(1,n+1):
#         a += 1
#         lst.append(a)
#     if i % 2 == 0:
#         lst = reversed(lst)
#     for z in lst:
#         print(f"{z:>{ln}d}", end=' ')
#     lst = []
#     print()
# ************************************************************************
# Задача 1
# Создать декоратор, который вычисляет и выводит (через print) время работы декорируемой функции
# При каждом вызове декорируемой функции печатать имя функции и сколько она выполнялась.
#
# from datetime import datetime
#
#
# def times(func):
#     counters = {}
#
#     def wrapper(*args, **kwargs):
#         counters[func] = counters.get(func, 0) + 1
#         start = datetime.now()
#         res = func(*args, **kwargs)
#         end = datetime.now() - start
#         print(f"время работы функции: {func.__name__}: {end}")
#         print(f'функция {func.__name__} вызвана {counters[func]} раз')
#         return res
#
#     return wrapper
#
#
# @times
# def iter(n, b):
#     lst = []
#     for i in range(n ** b):
#         if i % 2 == 0:
#             lst.append(i)
#
#     return lst
#
#
# p1 = iter(2, 25)
# print(p1)
# ************************************************************************
# Задача 2
# Изучить функцию wraps (from functools import wraps) и применить её к декоратору из прошлой задачи

# from datetime import datetime
# from functools import wraps
#
# def times(func):
#     counters = {}
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         counters[func] = counters.get(func, 0) + 1
#         res = func(*args, **kwargs)
#         print(f"время работы функции: {func.__name__}")
#         print(f'функция {func.__name__} вызвана {counters[func]} раз')
#         return res
#
#     return wrapper
#
#
# @times
# def iter(n, b):
#     """Функция итерирует диапазон от 0 до числа n в степени b  """
#     start = datetime.now()
#     lst = []
#     for i in range(n ** b):
#         if i % 2 == 0:
#             lst.append(i)
#     end = datetime.now() - start
#     print(end)
#     return lst
#
#
# p1 = iter(2, 6)
# print(iter.__name__)
# print(iter.__doc__)
# print(p1)

# Задача 3
# Задача со звёздочкой)
# Создать декоратор, оптимизирующий работу декорируемой функции.
# Декоратор должен сохранять результат работы функции на ближайшие 5 запусков и вместо выполнения функция возвращать
# сохранённый результат. После N запусков функция должна вызываться вновь, а результат работы
# функции — вновь кешироваться.

# hash = dict()
# count = 0
# 
# 
# def decor(func):
#     global count
#     count += 1
#     hash[count] = func
#     if count == 5:
#         count = 0
#         hash.clear()
#         print('словарь заполнен')
#     return hash
# 
# 
# def one(a, b):
#     mult = a ** b
#     print('функция one')
#     return decor(mult)
# 
# 
# one(2, 1)
# one(2, 1)
# one(2, 1)
# # one(2, 4)
# # one(2, 5)
# # one(2, 6)
# print(hash)
# *********************************************************************************************************************
#                                                  20.02.2023
# ********************************************************************************************************************
# Создайте декоратор, который запрещает выполнение функции, если её аргументы не удовлетворяют заданному условию.
# Например, если функция принимает числовой аргумент, то декоратор может запретить выполнение, если аргумент меньше
# нуля.

# def two(func):
#     def three(a):
#         if a > 0:
#             return func(a)
#         else:
#             return 'ошибка'
#
#     return three
#
#
# @two
# def one(a):
#     return a ** 2
#
#
# print(one(-2))
# print(one(5))
# ********************************************************************************************************************
# Создайте декоратор, который повторяет выполнение функции, если она выбрасывает исключение определенного типа.
# Например, если функция выбрасывает исключение ValueError, то декоратор может повторить выполнение функции несколько
# раз, пока она не выполнится успешно.
# ________ нет решения ______________
# ********************************************************************************************************************
# Создайте декоратор, который добавляет аргументы к вызову функции. Например, если функция принимает аргумент x,
# то декоратор может добавить аргумент y и вызвать функцию с аргументами x и y.

# def decor(func):
#     def wrapper(x):
#         y = 10
#         res = func(x + y)
#         return res
#
#     return wrapper
#
#
# @decor
# def one(x):
#     return x ** 2
#
#
# print(one(2))
# ********************************************************************************************************************
# Создайте декоратор, который позволяет выполнить функцию только при определенных условиях. Например, если
# функция принимает аргумент x, то декоратор может запретить выполнение функции, если x не является строкой.

# def decor(func):
#     def wrapper(x):
#         if isinstance(x, str):
#             func(x)
#         else:
#             print('ошибка')
#
#     return wrapper
#
#
# @decor
# def one(x):
#     print(x)
#
#
# one(1)
# ********************************************************************************************************************
# Напишите функцию-генератор, которая возвращает первые N чисел Фибоначчи.
# def fib(n):
#     fib1 = fib2 = 1
#     for i in range(2, n):
#         fib1, fib2 = fib2, fib1 + fib2
#         yield fib2
# fibs = fib(15)
# next(fibs)
# next(fibs)
# ********************************************************************************************************************
# Напишите класс-итератор. Объекты которого генерируют случайные числа. В количестве и в диапазоне,
# которые передаются с помощью аргументов.

# ********************************************************************************************************************
# Напишите итератор, который обходит элементы списка в обратном порядке.
# lst = []
#
# def rev(s):
#     for i in reversed(s):
#         lst.append(i)
#     ls = iter(lst)
#     try:
#         while True:
#             new_lst = next(ls)
#             print(new_lst)
#     except StopIteration:
#         print('итерация закончена')
#
# rev([1, 2, 3, 4, 5])

# ********************************************************************************************************************
# Напишите функцию, которая принимает два списка и возвращает список, содержащий элементы, которые присутствуют
# в обоих списках.
# ls = []
#
#
# def lst(lst, lst2):
#     for i in lst:
#         for j in lst2:
#             if i == j:
#                 ls.append(i)
#                 yield ls
#
#
# get = lst([1, 2, 3, 4, 5], [2, 4, 5, 6, 7])
# print(next(get))
# print(next(get))

# ********************************************************************************************************************
# Напишите функцию-генератор, которая возвращает все простые числа в диапазоне от 2 до N.
# def simple(n):
#     for i in range(2, n + 1):
#         for j in lst:
#             if i % j == 0:
#                 break
#         else:
#             yield i
#
#
# gen = simple(15)
# print(next(gen))
# print(next(gen))

# ********************************************************************************************************************
# Напишите функцию, которая принимает итератор и функцию, и возвращает новый итератор,
# который применяет функцию к каждому элементу последовательности.
# lst = []
# it = iter([1, 2, 3, 4, 5])
# def one(a):
#     return a ** 2
#
#
# def two(it, one):
#     for i in it:
#         lst.append(one * i)
#     return iter(lst)

# two(it, one(5))

# ********************************************************************************************************************
# Напишите функцию-генератор, которая возвращает все совершенные числа
# (числа, равные сумме своих делителей, не считая себя) в диапазоне от 1 до N.
# def one(n):
#     sums = 0
#     for i in range(1, n + 1):
#         for j in range(1, i):
#             if i % j == 0:
#                 sums += j
#         if sums == i:
#             yield i
#         sums = 0
#
#
# a = one(28)
# next(a)
# next(a)

# ********************************************************************************************************************
# Напишите генератор, который создает последовательность случайных чисел от 0 до 100 и
# позволяет изменять шаг генерации с помощью метода send().
# from random import randrange
#
# def one():
#     b = 1
#     while True:
#         a = randrange(0, 101, b)
#         b = yield
#
#
# z = one()
# next(z)
# z.send(100)
# z.send(1)
#
# *********************************************************************************************************************
#                   1.03.2023
# *********************************************************************************************************************

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
