# Объектно-ориентированное программирование

# class Person:
#     pass
#
# tom = Person()
# bob = Person()

#
# class Person:
#     #конструктор
#     def __init__(self):
#         print("Создание объекта Person")
#
# tom = Person()  #Создание объекта Person


#Атрибуты объекта

# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# tom = Person("Tom", 22)
#
# print(tom.name)
# print(tom.age)
#
# tom.age = 37
# print(tom.age)

#Методы классов

# class Person:
#     def say_hello(self):
#         print("Hello")
#
# tom = Person()
# tom.say_hello()
#
#
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name  # имя человека
#         self.age = age  # возраст человека
#
#     def display_info(self):
#         print(f"Name: {self.name}  Age: {self.age}")
#
#
# tom = Person("Tom", 22)
# tom.display_info()  # Name: Tom  Age: 22
#
# bob = Person("Bob", 43)
# bob.display_info()  # Name: Bob  Age: 43
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#         print("Создан человек с именем", self.name)
#
#     def __del__(self):
#         print("Удален человек с именем", self.name)
#
# tom = Person("Tom")

# class Person:
#
#     def __init__(self, name):
#         self.name = name
#         print("Создан человек с именем", self.name)
#
#     def __del__(self):
#         print("Удален человек с именем", self.name)
#
#
# def create_person():
#     tom = Person("Tom")
#
# create_person()
# print("Конец программы")

 #Инкапсуляция, атрибуты и совйства

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_person(self):
#         print(f"Имя: {self.name}\tВозраст: {self.age}")
#
#
# tom = Person("Tom", 39)
# tom.name = "Человек-паук"
# tom.age = 100
# tom.print_person()
#
#
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def print_person(self):
#         print(f"Имя: {self.__name}\tВозраст: {self.__age}")
#
#
# tom = Person("Tom", 39)
# tom.__name = "Человек-паук"
# tom.__age = 100
# tom.print_person()

#Методы доступа. Геттеры и сеттеры

class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст

    # сеттер для установки возраста
    def set_age(self, age):
        if 0 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    # геттер для получения возраста
    def get_age(self):
        return self.__age

    # геттер для получения имени
    def get_name(self):
        return self.__name

    def print_person(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


tom = Person("Tom", 39)
tom.print_person()  # Имя: Tom  Возраст: 39
tom.set_age(-3486)  # Недопустимый возраст
tom.set_age(25)
tom.print_person()  # Имя: Tom  Возраст: 25






  

































































































































































