# name = input("Введите ваше имя: ")
# print("Привет,", name)
#
# if 1 < 2:
#     print("1<2")
# # comment
# # comment
# '''
# comment
# '''
# print(input("привет"))
# b = True
# if b:
#     print(123)
# c = 10
# d = 0b10
# print(c+d)
# x = 0.9e-30
# print(x)
# message = "Hello World!"
# print(message)  # Hello World!
# name = 'Tom'
# print(name)  # Tom
# text = ("Laudate omnes gentes laudate "
#         "Magnificat in secula ")
# print(text)
# text = '''Laudate omnes gentes laudate
# Magnificat in secula
# Et anima mea laudate
# Magnificat in secula
# '''
# print(text)
# userName = "Tom"
# userAge = 37
# user = f"name: {userName}  age: {userAge}"
# print(user)   # name: Tom  age: 37
# userId = "abc"  # тип str
# print(type(userId))  # <class 'str'>
# userId = 234  # тип int
# print(type(userId))  # <class 'int'>
# g = 0b101
# print(g)
# print(f"{g:0b}")
# print(f"{g:0d}")
# f = 0b10101
# d = 0b11010
# a = f & d
# print(a)
# print(a)
# a = 6
# print(~a)
# if language == "english":
#     print("English")
#     if daytime == "morning":
#         print("Good morning")
#     else:
#         print("Good evening")
# mes = "123qwe123"
# for b in mes:
#     print(b, end="")
# i = 1
# j = 1
# while i < 10:
#     while j < 10:
#         print(i * j, end="\t")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1
# def sum(*numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     print(f"sum = {result}")
#
#
# sum(1, 2, 3, 4, 5)  # sum = 15
# sum(3, 4, 5, 6)  # sum = 18
# def maxim(*numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     print(result)
#

# maxim(101, 2, 3, 4)
# def prnt(asd): print(asd)
# qwe = prnt
# def do_operation(a, b, oper):
#     print(oper(a, b))
#
#
# do_operation(333, 2, lambda a, b: a * b)
# a = "2"
# b = 2
# print(a+str(b))
# def outer():  # внешняя функция
#     n = 5
#
#     def inner():  # вложенная функция
#         print(n)
#
#     inner()  # 5
#     print(n)
#
#
# outer()  # 5
# def outer():  # внешняя функция
#     n = 5
#
#     def inner():  # вложенная функция
#         n = 25
#         print(n)
#
#     inner()  # 25
#     print(n)
#
#
# outer()  # 5
# 25    - inner
# 5     - outer
# def outer():  # внешняя функция
#     n = 5
#
#     def inner():  # вложенная функция
#         nonlocal n  # указываем, что n - это переменная из окружающей функции
#         n = 25
#         print(n)
#
#     inner()  # 25
#     print(n)
#
#
# outer()  # 25
# def outer():  # внешняя функция
#     n = 5  # лексическое окружение - локальная переменная
#
#     def inner():  # локальная функция
#         nonlocal n
#         n += 1  # операции с лексическим окружением
#         print(n)
#
#     return inner
#
# tmp = outer()
# tmp()
# tmp()
# tmp()
# tmp()
# tmp1 = outer()
# tmp1()
# tmp1()
# tmp1()
# tmp1()
# class Person:
#     def say(self, message):
#         print(message)
#
#     def sayHello(self):
#         self.say("Q")
#
#
# asd = Person()
# asd.say("asd")
# asd.sayHello()
#
#
# class Person:
#
#     def say(self, message):
#         print(message)
#
#     def say_hello(self):
#         self.say("Hello work")  # обращаемся к выше определенному методу say
#
#
# tom = Person()
# tom.say_hello()
# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = 1
#
#     def say(self):
#         print("yo-la")
#         print(f"my name {self.__name} ama {self.__age} butcher")
#
#     def __set_name__(self, name):
#         self.__name = name
#
#
# tom = Person("tom")
# class Person:
#     def __init__(self):
#         # self.__name = name
#         # self.__age = age
#         self.__name = None
#         print("gogo")
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     def say(self):
#         print(f"{self.__name}")
#
#
# class Worker(Person):
#     def say(self):
#         super().say()
#         super(Worker, self).say()
#         print("qweqwe1")
#
#
# tom = Person()
# tom.name = "assdd"
# tom.say()
# tom.__set_name__("ann")
# tom.say()
# tom.name = "qweqwe"
# print(tom.name)
#
# bob.name = "bob"
# bob = Worker()
# bob.say()
# tom.say()
# numbers = [1, 2, 3, 4, 5, 6, 0]
# print(sorted(numbers))
# print(numbers)
# numbers = range(0, 10, 2)
# print(numbers)
# for i in range(1, 3):
#     print(i, end=" ")
numbers = {
    1: 123,
    2: 234,
    3: 345,
    4: 456
}
for key in numbers.values():
    print(key)
