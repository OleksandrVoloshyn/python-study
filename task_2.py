# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
#
# запишите 5 тудушек
# и выведете все

# def notebook():
#     todo_list = []
#
#     def add_todo(todo):
#         nonlocal todo_listпротипизировать первое задание
#         todo_list.append(todo)
#
#     def get_all():
#         return todo_list
#
#     return add_todo, get_all
#
#
# add, get = notebook()
#
# add('just')
# add('do')
# add('it')
# add('something')
# add('xxx')
# print(get())

# *******************************************************************************************************
# протипизировать первое задание

# from typing import Callable
#
#
# def notebook() -> [Callable[[str], None], Callable[[], list[str]]]:
#     todo_list: list[str] = []
#
#     def add_todo(todo: str) -> None:
#         nonlocal todo_list
#         todo_list.append(todo)
#
#     def get_all() -> list[str]:
#         return todo_list
#
#     return add_todo, get_all
#
#
# add, get = notebook()
#
# add('just')
# add('do')
# add('it')
# add('something')
# add('xxx')
# print(get())

# ******************************************************************************
# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
# Пример:
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

#
# def expanded_form(num: int | str) -> str:
#     res: list[str] = []
#
#     def inner(str_num: str):
#         if str_num[0] in '123456789':
#             res.append(str_num[0] + ('0' * (len(str_num) - 1)))
#             if len(str_num) > 1:
#                 inner(str_num[1:])
#
#         if str_num[0] == '0' and len(str_num) > 1:
#             inner(str_num[1:])
#
#     inner(str(num))
#     return ' + '.join(res)
#
#
# print(expanded_form('12'))
# print(expanded_form('42'))
# print(expanded_form('70304'))

# ******************************************************************************
# создать декоратор который будет считать сколько раз была запущена функция
# и будет выводит это значение после каждого запуска функции
#
# def decor(func):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(f'count: {count}')
#         func()
#         print('*' * 20)
#
#     return inner
#
#
# @decor
# def func1():
#     print('func1')
#
#
# @decor
# def func2():
#     print('func2')
#
#
# func1()
# func1()
# func2()
# func1()
# func2()
# func2()

# ************************************ADITIONAL****************************************
# сделайте функцию на замыкания которая будет возвращать декоратор который будет считать
# общее количество запущенных  функций декорированных этим декоратором

# def closures():
#     count = 0
#
#     def decor(func):
#         def inner():
#             nonlocal count
#             count += 1
#             print(count)
#             func()
#             print('*' * 20)
#
#         return inner
#
#     return decor
#
#
# decorator = closures()
#
#
# @decorator
# def func1():
#     print('func1')
#
#
# @decorator
# def func2():
#     print('func2')
#
#
# func1()
# func1()
# func2()

# *********************************************************************
# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)
# def fib(l):
#     res = [1]
#
#     def init(x=1, y=1):
#         res.append(y)
#         if len(res) < l:
#             init(y, x + y)
#
#     init()
#     return res
#
#
# print(fib(10))

# **********************************************************************************
# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3

# def count_nums(num):
#     res = {'pare': 0, 'not': 0}
#     for i in str(num):
#         if i in '02468':
#             res['pare'] += 1
#         if i in '13579':
#             res['not'] += 1
#
#     return f'num = {num} -> п = {res["pare"]},н = {res["not"]} ;'
#
#
# print(count_nums(225688))
#  ***************************************************************************
# прога, що виводить кількість кожного символа  з введеної строки,
# наприклад:
# st = 'as 23 fdfdg544'

# введена строка
# 
# 'a' -> 1  # вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2
# def func(s: str) -> None:
#     trash: list[str] = []
#     for i in s:
#         if i not in trash:
#             print(f'{i} -> {s.count(i)}')
#             trash.append(i)
#
#
# func(st)

# **********************************************************************************
# генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
# задача сделать c него лист листов такого плана:
#
l = [i for i in range(1, 19, 2)]

# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]
# def func(num_list: list):
#     res = []
#     x = 0
#     y = 1
#     count = 2
#     while y <= len(num_list):
#         res.append(num_list[x:y])
#         x, y = y, y + count
#         count += 1
#     res.append(num_list[x:])
#     return res
#
#
# print(func(l))

# *************************************************************************************
# найти со списка только уникальные числа#
# пример [1,2,3,4,2,5,1] => [ 3, 4, 5 ]
# l = [1, 2, 3, 4, 2, 5, 1]
#
#
#
#
# def func(nums_list: list):
#     res = set()
#     for num in nums_list:
#         if nums_list.count(num) == 1:
#             res.add(num)
#     return list(res)
#
#
# print(func(l))

# если с этим справитесь то усложняем...
# методом count пользоваться нельзя
# l = [1, 2, 3, 4, 2, 5, 1]
#
# def func(nums_list: list):
#     res = list()
#     trash = list()
#     for num in nums_list:
#         if (num not in res) and (num not in trash):
#             res.append(num)
#         else:
#             trash.append(num)
#             res.remove(num)
#     return res
#
# print(func(l))
