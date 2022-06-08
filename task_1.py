# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = 'as 23 fdfdg544'
# res = ''
# for i in st:
#     if i.isdigit():
#         res += i
# print(', '.join(res))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34'
# res = ''
# for i in st:
#     if i.isdigit():
#         res += i
#     else:
#         res += ' '
# print(', '.join(res.split()))

# #################################################################################
#
# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# res = [i.upper() for i in greeting]
# print(res)

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# res = [i ** 2 for i in range(0, 50) if i % 2]
# print(res)

# function
#
# - створити функцію яка виводить ліст
# def print_list(el):
#     print(el)
#
#
# print_list([1, 2, 3, 4])

# - створити функцію яка приймає три числа та виводить та повертає найменьше.
# def print_get_min(one, two, three):
#     res = min(one, two, three)
#     print(res)
#     return res
#
#
# print_get_min(1, 2, 3)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def print_get_max(one, two, three):
#     res = max(one, two, three)
#     print(res)
#     return res
# print_get_max(1,2,3)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def print_max_get_min(*args):
#     print(max(args))
#     return min(args)
#
#
# print(print_max_get_min(1, 2, 3, 4, 5, 6))

# - створити функцію яка повертає найбільше число з ліста
# def get_max_from_list(l):
#     return max(l)
#
# print(get_max_from_list([1, 2, 3, 4, 5]))

# - створити функцію яка повертає найменьше число з ліста
# def get_min_from_list(l):
#     return min(l)
#
# print(get_min_from_list([1, 2, 3, 4, 5]))

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# def get_count_from_list(l):
#     return sum(l)
#
# print(get_count_from_list([1, 2, 3, 4, 5]))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def get_avg_from_list(l):
#     return sum(l) / len(l)
#
# print(get_avg_from_list([1, 2, 3, 4, 5, 6]))

# #################################################################################################
# 1)Дан лист:
# l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

#   - найти min число в листе
# print(min(l))
#   - удалить все дубликаты в листе
# def remove_duplicate(l):
#     for num in l:
#         if l.count(num) > 1:
#             l.remove(num)
#             remove_duplicate(l)
# remove_duplicate(l)
# print(l)

#   - заменить каждое четвертое значение на "Х"
# for i in range(3, len(l), 4):
#     l[i] = 'X'
# print(l)

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# side = 10
# i = side
# while i >= 1:
#     if i == side or i == 1:
#         j = side
#         while j > 0:
#             print('*', end='')
#             j -= 1
#         print()
#     else:
#         j = side - 2
#         print('*', end='')
#         while j > 0:
#             print(' ', end='')
#             j -= 1
#         print('*')
#     i -= 1

# 3) вывести табличку умножения с помощью цикла while
# size = 10
# i = 1
# while i <= size:
#     j = 1
#     while j <= size:
#         res = i * j
#         if res // 10:
#             print(res, end='  ')
#         else:
#             print(res, end='   ')
#         j += 1
#     print()
#     i += 1

# 4) переделать первое задание под меню с помощью цикла
def remove_duplicate(target):
    for num in target:
        if target.count(num) > 1:
            target.remove(num)
            remove_duplicate(target)


def change_every_forth_on_x(target):
    for num in range(3, len(target), 4):
        target[num] = 'X'


def get_num_near_to_avg(target):
    avg = sum(target) / len(target)
    target.append(avg)
    target.sort()
    index = target.index(avg)

    smaller = target[index - 1]
    bigger = target[index + 1]
    different1 = bigger - avg
    different2 = avg - smaller
    return bigger if different1 < different2 else smaller


l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

while True:
    print('1) Найти min число в листе')
    print('2) Удалить все дубликаты в листе')
    print('3) Заменить каждое четвертое значение на "Х"')
    print('4) Вивести найблище число до середнього арефметичного')
    print('0) Вихід')
    choice = input('Зробіть свій вибір: ')

    if choice == '1':
        print(min(l))

    if choice == '2':
        list_copy = l.copy()
        remove_duplicate(list_copy)
        print(l, 'original', sep='-')
        print(list_copy, 'result', sep='-')

    if choice == '3':
        list_copy = l.copy()
        change_every_forth_on_x(list_copy)
        print(list_copy)

    if choice == '4':
        print(get_num_near_to_avg(l))

    if choice == '0':
        break
