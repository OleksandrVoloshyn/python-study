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
