# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон
# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_area(self):
#         return self.x * self.y
#
#     def __add__(self, other):
#         return self.get_area() + other.get_area()
#
#     def __sub__(self, other):
#         return self.get_area() - other.get_area()
#
#     def __eq__(self, other):
#         return self.get_area() == other.get_area()
#
#     def __ne__(self, other):
#         return self.get_area() != other.get_area()
#
#     def __lt__(self, other):
#         return self.get_area() < other.get_area()
#
#     def __gt__(self, other):
#         return self.get_area() > other.get_area()
#
#     def __len__(self):
#         return self.x + self.y
#
#
# r1 = Rectangle(5, 8)
# r2 = Rectangle(3, 4)
# print(r1 + r2)
# print(r1 - r2)
# print(r1 == r2)
# print(r1 != r2)
# print(r1 < r2)
# print(r1 > r2)
# print(len(r1))

###############################################################################
# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# в классе золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество

# from abc import ABC
#
#
# class Human(ABC):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Prince(Human):
#     def __init__(self, name, age, shoe):
#         super().__init__(name, age)
#         self.shoe = shoe
#
#     def find_love(self, arr):
#         res = []
#         for girl in arr:
#             if girl.foot_size == self.shoe:
#                 res.append(girl)
#
#         return res
#
#
# class Cinderella(Human):
#     count = 0
#
#     def __init__(self, name, age, foot_size):
#         super().__init__(name, age)
#         self.foot_size = foot_size
#         Cinderella.count += 1
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#         return self.name
#
#     @classmethod
#     def get_count(cls):
#         return f'created - {cls.count} Cinderellas'
#
#
# sasha = Prince('Sasha', '24', '40')
# olya = Cinderella('Olya', '20', '40')
# vitalik = Cinderella('vitalik', '28', '40')
# masha = Cinderella('Masha', '22', '39')
# ira = Cinderella('Ira', '18', '37')
#
# print(Cinderella.get_count())
# print(sasha.find_love([olya, masha, ira, vitalik]))

# *************************************************************************************************
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку
# чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# Приклад:
#
# Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))
#
#     Main.show_all_magazines()
#     print('-' * 40)
#     Main.show_all_books()

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Main:
    printable_list = []

    @classmethod
    def add(cls, item):
        if isinstance(item, Book) or isinstance(item, Magazine):
            cls.printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        res = []
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                res.append(item)
        return res

    @classmethod
    def show_all_books(cls):
        res = []
        for item in cls.printable_list:
            if isinstance(item, Book):
                res.append(item)
        return res


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

print(Main.show_all_magazines())
print('-' * 40)
print(Main.show_all_books())
