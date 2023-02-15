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
# ************************************************************************
# Задача 1
# Создать декоратор, который вычисляет и выводит (через print) время работы декорируемой функции
# При каждом вызове декорируемой функции печатать имя функции и сколько она выполнялась.

# from datetime import datetime
#
#
# def times(func):
#     counters = {}
#
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
# p1 = iter(10, 4)
# print(p1)
#************************************************************************
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