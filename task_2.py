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
