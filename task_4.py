# есть файл с email, ваша задача записать в новый текстовый файл только почты от @gmail.com

# try:
#     with open('emails.txt') as file:
#         correct_emails = []
#         candidates = file.read().split()
#         for candidate in candidates:
#             if candidate[-10:] == '@gmail.com':
#                 correct_emails.append(candidate)
#
#         if correct_emails:
#             with open('gmail_emails', 'w') as file2:
#                 for email in correct_emails:
#                     file2.write(email + '\n')
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

try:
    while True:
        print('1) Создать запись')
        print('2) Список все записей')
        print('3) Общая сумма всех покупок')
        print('4) Самая дорогая покупка')
        print('5) Поиск по названию покупки')
        print('9) Выход')

        choice = input('Зробіть ваш вибір: ')

        with open('db.txt', 'r') as file:
            try:
                db = list(json.load(file))
            except json.decoder.JSONDecodeError:
                db = list()

        match choice:
            case '1':
                purchase = input('Назва покупки: ')
                try:
                    price = int(input('Ціна: '))
                except ValueError as err:
                    print('price має бути числом')
                else:
                    try:
                        with open('db.txt', 'w') as file:
                            note = {'purchase': purchase, 'price': price}
                            db.append(note)
                            json.dump(db, file)
                    except Exception as err:
                        print(err)

            case '2':
                for obj in db:
                    print(obj)

            case '3':
                count = 0
                for obg in db:
                    count += obg['price']

                print(f'{count=}')

            case '4':
                res = {'purchase': None, 'price': 0}
                for candidate in db:
                    if candidate['price'] > res['price']:
                        res = candidate
                print(res)

            case '5':
                search_name = input('Імя для пошуку: ')
                res = 'Результат відсутній'
                for obj in db:
                    if obj['purchase'] == search_name:
                        res = obj

                print(res)

            case '9':
                print('Вихід')
                exit()

except KeyboardInterrupt as err:
    print('\n Вихід')
