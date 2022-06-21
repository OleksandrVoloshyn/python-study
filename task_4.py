# есть файл с email, ваша задача записать в новый текстовый файл только почты от @gmail.com

# try:
#     with open('emails.txt') as file, open('gmail_emails', 'a') as res_file:
#         for line in file:
#             email = line.split()[-1]
#             if email.endswith('@gmail.com'):
#                 print(email, file=res_file)
# except FileNotFoundError as err:
#     print(err)
# except Exception as err:
#     print(err)

# ******************************************************************************************
# 2) для хранения и чтения данных использовать файлы
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
import json
from typing import TypedDict

NoteType = TypedDict('NoteType', {'purchase': str, 'price': int})


class Note:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__store: list[NoteType] = []
        try:
            with open(file_name) as file:
                self.__store: list[NoteType] = json.load(file)
        except:
            pass

    def add(self):
        try:
            with open(self.__file_name, 'w') as file:
                purchase = input('Введіть назву покупки: ')
                price = ''
                while not price.isdigit():
                    price = input('Введіть ціну покупки: ')
                self.__store.append({'purchase': purchase, 'price': int(price)})
                json.dump(self.__store, file)
        except Exception as err:
            print(err)

    def show_all(self):
        if not self.__store:
            print('Записи відсутні')
            return

        for item in self.__store:
            print(item)

    def sum_of_cost(self):
        sum_cost = sum(item['price'] for item in self.__store)
        print(f'{sum_cost=}')

    def most_expensive(self):
        print(max(self.__store, key=lambda item: item['price']))

    def find_by_name(self):
        find = input('Введіть назву покупки: ')
        for item in self.__store:
            if item['purchase'].lower() == find.lower():
                print(item)
                return

        print('Нічого не знайдено')


note = Note('purchases.json')
while True:
    print('1) Создать запись')
    print('2) Список все записей')
    print('3) Общая сумма всех покупок')
    print('4) Самая дорогая покупка')
    print('5) Поиск по названию покупки')
    print('9) Выход')

    choice = input('Зробіть ваш вибір: ')

    match choice:
        case '1':
            note.add()
        case '2':
            note.show_all()
        case '3':
            note.sum_of_cost()
        case '4':
            note.most_expensive()
        case '5':
            note.find_by_name()
        case '9':
            break
        case _:
            print('Неправильно в введені дані')
