# from email.utils import encode_rfc2231
#
# print("_____\n\"1 lesson\"")
# #name = input("Введите ваше имя: ")
# #print("Привет,", name)
# print(7+12)
# print("Hello")
# if 1 < 2:
#     print("Hello")
# '''
#     Вывод на консоль
#     сообщения Hello World
# '''
# print("Hello World") # Message
# print("Full name:", "Alfar", "Gadilchinov")
# '''
#     Переменные и типы данных
# '''
# print("_____\n\"2 lesson\"")
# name = "Tom"
# print(name)
# name = "Tom"
# print(name)
# name = "Bob"
# print(name)
# isMarried = False
# print(isMarried) # False
# isAlive = True
# print(isAlive)   # True
# '''
#     Целые числа
# '''
# age = 18
# print("Возраст:", age) # Возраст: 21
# count = 15
# print("Количество:", count) # Количество: 15
# studCount = 28
# print("Количество студентов:", studCount) # Количество студентов: 28
# a = 0b11
# b = 0b1011
# c = 0b100001
# print(a) # (изн 2-чная) )3 в 10-чной сист
# print(b) # (изн 2-чная) 11 в 10-чной сист
# print(c) # (изн 2-чная) 33 в 10-чной сист
# a = 0o7
# b = 0o11
# c = 0o17
# print(a) # (изн 8-чная) 7 в 10-чной сист
# print(b) # (изн 8-чная) 9 в 10-чной сист
# print(c) # (изн 8-чная) 15 в 10-чной сист
# a = 0x0A
# b = 0xFF
# c= 0xA1
# print(a) # (изн 16-чная) 10 в 10-чной сист
# print(b) # (изн 16-чная) 255 в 10-чной сист
# print(c) # (изн 16-чная) 161 в 10-чной сист
# '''
#     Дробные числа
# '''
# height = 1.68
# pi = 3.14
# weight = 68.
# print(height) # 1.68
# print(pi)     # 3.14
# print(weight) # 68.0
# #Число с плавающей точкой в эксп зап
# x = 3.9e3
# print(x) # 3900.0
# x = 3.9e-3
# print(x) # 0.0039
# '''
#     Комплексные числа
# '''
# complexNumber = 1+2j
# print(complexNumber) # (1+2j)
# '''
#     Строки
# '''
# message = "Hello World!"
# print(message) # Hello World!
# name = 'Tom'
# print(name) # Tom
# text = ("Laudate omnes gentes laudate "
#         "Magnificat in secula ")
# print(text)
# '''
# Это комментарий
# '''
# text = '''Laudate omnes gentes laudate
# Magnificat in secula
# Et anima mea laudate
# Magnificat in secula
# '''
# #Три кавычки в перем это не комм
# '''
#     Управляющие последовательности
#     в строке
# '''
# print(text)
# text = "Message:\n\"Hello World\""
# print(text)
# path = r"C:\python\name.txt"
# print(path)
# dvaSlesha = "Dva\\Slesha"
# print(dvaSlesha)
# sleshSKav = "Slesh\'SKav"
# print(sleshSKav)
# sleshSDvKav = "Slesh\"SDvKav"
# print(sleshSDvKav)
# sleshSN = "Slesh\nSn"
# print(sleshSN)
# sleshST = "Slesh\tSt"
# print(sleshST)
# '''
#     Вставка значений в строку
# '''
# userName = "Tom"
# userAge = 37
# user = f"name: {userName} age: {userAge}"
# print(user)
# #f как бы fake-значение, оно просто
# #выводит здесь 2 в 1-м
# #P.S, оказалось F от формат
# '''
#     Динамическая типизация
# '''
# userId = "abc" # str
# print(userId)
# userId = 234 # int
# print(userId)
# #А вот как узнать текущий тип
# userId = "abc" # str
# print(type(userId)) # <class 'str'>
# userId = 234 # int
# print(type(userId)) # <class 'int'>
# print("_____\n\"3 lesson\"")
# '''
#     Консольный ввод
# '''
# #name = input("Введите своё имя: ")
# #print(f"Ваше имя: {name}")
# #Теперь больше значений
# #name = input("Your name: ")
# #age = input("Your age: ")
# #print(f"Name: {name} Age: {age}")
# '''
#     Арифметические операции с числами
# '''
# print(6 + 2) #сложение
# print(6 - 2) #вычитание
# print(6 * 2) #умножение
# print(6 / 2) #деление
# print(7 / 2) #целочисл делен
# print(7 // 2) #целочисл делен
# print(6 ** 2) #возведение в степень
# print(7 % 2) #остаток от деления
# '''
#     Операции по приоритету (по убыв)
# ** Справо налево.
# * / // % Слева направо.
# + - Слева направо.
# '''
# number = 3 + 4 * 5 ** 2 + 7
# print(number)
# #3 + ( (5 ** 2) * 4 )
# #Переопределим порядок
# number = (3 + 4) * (5 ** 2 + 7)
# print(number)
# '''
#     Арифметические операции с присвоением
# '''
# #+= Присвоение рез сложения
# #-= Присвоение рез вычитания
# #*= Присовоение рез умножения
# #/= Присвоение рез от делен
# #//= Присвоение рез целочисл делен
# #**= Присвоение степени числа
# #%= Присвоение остатка от делен
# number = 10
# number /= 2
# print(number)
# number -=3
# print(number)
# number *=72
# print(number)
# '''
#     Округление и функция round
# '''
# first_number = 2.0001
# second_number = 5
# third_number = first_number / second_number
# print(third_number)
# print(2.0001 + 0.1)
# #Округляем
# first_number = 2.0001
# second_number = 0.1
# third_number = first_number + second_number
# print(round(third_number))
# #round примет 2-е число
# #оно значит сколько зн. после зап.
# first_number = 2.0001
# second_number = 0.1
# third_number = first_number + second_number
# print(round(third_number, 4))
# #До целого числа
# print(round(2.49)) #до ближ. целого 2
# print(round(2.51)) #3
# #Если округляемая часть равно удалена,
# #округляется к ближ. чётному
# print(round(2.5))
# print(round(3.5))
# #Округление до двух зн посл зап.
# print(round(2.554, 2))
# print(round(2.5551, 2))
# print(round(2.554999, 2))
# print(round(2.499, 2))
# #10-чная часть числа не может быть
# #точной в виде числа float,
# #это приводит к другим результатам
# print(round(2.545, 2))
# print(round(2.555, 2))
# print(round(2.565, 2))
# print(round(2.575, 2))
# #и теперь до не чётных
# print(round(2.655, 2))
# print(round(2.665, 2))
# print(round(2.675, 2))
# print("_____\n\"lesson 4\"")
# '''
#     Условные выражения
# '''
# '''
#     Операции сравнения
# '''
# #== Возвращает True, если оба операнда равны. Иначе False
# #!= Возвращает True, если оба операнда НЕ равны. Иначе False
# #> Возвращает True, если первый операнд больше второго
# #< Возвращает True, если первый операнд меньше второго
# #>= Возвращает True, если первый операнд больше или равен второму
# #<= Возвращает True, если первый операнд меньше или равен второму
# a = 5
# b = 6
# result  = 5 == 6 # сохран результ
# print(result) #f
# print(a != b) #t
# print(a > b) #f
# print(a < b) #t
#
# bool1 = True
# bool2 = False
# print(bool1 == bool2) # F
# '''
#     Логические операции
# '''
# x and y
#
# age = 22
# weight = 58
# result = age > 21 and weight == 58
# print(result) #True
#
# result = 4 and "w"
# print(result) ## w, так как 4 равно True, поэтому возвращается значение последнего операнда
#
# result = 0 and "w"
# print(result) #0, так как 0 эквивалентно False
#
# x or y
#
# age = 22
# isMarried = False
# result = age > 21 or isMarried
# print(result) # True, так как выражение age > 21 равно True
#
# result = 4 or "w"
# print(result) #4, так как 4 эквивалентно True, поэтому возвращается значение первого операнда
#
# result = 0 or "w"
# print(result) # w, так как 0 эквивалентно False, поэтому возвращается значение последнего операнда
#
# # not
# #логическое отрицание
#
# age = 22
# isMarried = False
# print(not age > 21) #False
# print (not isMarried) #True
# print(not 4) #False
# print(not 0) #True
#
# # in
#
# message = "hello world!"
# hello = "hello"
# print(hello in message)  # True - подстрока hello есть в строке "hello world!"
#
# gold = "gold"
# print(gold in message) # False - подстроки "gold" нет в строке "hello world!"
#
# # not in
#
# message = "hello world!"
# hello = "hello"
# print(hello not in message)  # False
#
# gold = "gold"
# print(gold not in message)  # True

# Условная конструкция if

# if логическое_выражение:
#     инструкции
# [elif логическое выражение:
#     инструкции]
# [else:
#     инструкции]

# language = "english"
# if language == "english":
#     print("Hello")
# print("End")
#
# # Блок else
#
# language = "russian"
# if language == "english":
#     print("Hello")
# else:
#     print("Привет")
# print("End")
#
# # elif
#
# language = "german"
# if language == "english":
#     print("Hello")
#     print("World")
# elif language == "german":
#     print("Hallo")
#     print("Welt")
# else:
#     print("Привет")
#     print("мир")
#
# # Вложенные конструкции if
#
# language = "english"
# daytime = "morning"
# if language == "english":
#     print("English")
#     if daytime == "morning":
#         print("Good morning")
#     else:
#         print("Good evening")
#
# # Циклы while и for
#
# # while условное_выражение:
# #     ИНСТРУКЦИИ
#     number = 1
#
#     while number < 5:
#         print(f"number = {number}")
#         number += 1
#     print("Работа программы завершена")
#
#
#     number = 1
#
#     while number < 5:
#         print(f"number = {number}")
#         number += 1
#     else:
#         print(f"number = {number}. Работа цикла завершена")
#     print("Работа программы завершена")
#
#     # Цикл for
#     # for переменная in набор_значений:
#     #   инструкции
#
#     message = "Hello"
#
#     for c in message:
#         print(c)
#
# # Нередко в связке с циклом for применяется встроенная функция range(), которая генерирует числовую последовательность:
#
# for n in range(10):
#     print(n, end=" ")
#
# # Также в функцию range() можно передать третий параметр, который указывает на приращение:
#
# for n in range(0, 10, 2):
#     print(n, end=" ")
#
# message = "Hello"
# for c in message:
#     print(c)
# else:
#     print(f"Последний символ:{c}. Программа завершена");
# print("Программа завершена")

i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1
    #
    # for c1 in "ab":
    #     for c2 in "ba":
    #         print(f"{c1}{c2}")

# Выход из цикла. break и continue

# number = 0
# while number < 5:
#     number += 1
#     if number == 3 :
#         break
#     print(f"number = {number}")

# number = 0
# while number < 5:
#     number += 1
#     if number == 3 :
#         continue
#     print(f"number ={number}")
#

number = input("Введите певое число: ")
number2 = input("Введите второе число: ")
for c in number:
    
