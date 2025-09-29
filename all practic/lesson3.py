# # function
# def say_hello():
#     print("Hello") # Пример простейшей функции
#
# def say_hello(): # определение функции say_hello
#     print("Hello")
#
# say_hello() # вызов функции
# say_hello()
# say_hello()
#
#
# def say_hello(): print("Hello") #Если функция имеет одну инструкцию, то ее можно разместить на одной строке с остальным определением функции:
#
# say_hello()
#
#
# def say_hello():
#     print("Hello")
#
# def say_goodbye():
#     print("Good Bye")
#
# say_hello()
# say_goodbye()
#
#
# def print_messages():
#     # определение локальных функций
#     def say_hello(): print("Hello")
#     def say_goodbye(): print("Good Bye")
#     # вызов локальных функций
#     say_hello()
#     say_goodbye()
#
# # вызов функции print_messages
# print_messages()
# #say_hello() # вне функции print_messages функция say_hello не доступна
#
# def main():
#     say_hello()
#     say_goodbye()
#
# def say_hello():
#     print("Hello")
#
# def say_goodbye():
#     print("Good Bye")
#
# # вызов функции main
# main()
#
# # Параметры функции
#
# def say_hello(name): # Теперь определим и используем свою функцию с параметрами
#     print(f"Hello, {name}")
#
# say_hello("Tom")
# say_hello("Bob")
# say_hello("Alice")
#
# def print_person(name, age):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#
# print_person("Tom", 37)
#
# # Значения по умолчанию
#
# def say_hello(name="Tom"):
#     print(f"Hello, {name}")
#
# say_hello()
# say_hello("Bob")
#
#
# def print_person(name, age = 18):
#     print(f"Name: {name} Age: {age}")
#
# print_person("Bob")
# print_person("Tom", 37)
#
#
# def print_person(name="Tom", age=18):
#     print(f"Name: {name}  Age: {age}")
#
#
# print_person()  # Name: Tom  Age: 18
# print_person("Bob")  # Name: Bob  Age: 18
# print_person("Sam", 37)  # Name: Sam  Age: 37
#
#
# # Передача значений параметрам по имени. Именованные параметры
#
# def print_person(name, age):
#     print(f"Name: {name} Age: {age}")
#
# print_person(age = 22, name = "Tom")
#
# def print_person(name, *, age, company):
#     print(f"Name: {name} Age: {age} Company: {company}")
#
# print_person("Bob", age = 41, company = "Microsoft")
#
#
# def print_person(name, /, age, company="Microsoft"):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Tom", company="JetBrains", age=24)  # Name: Tom  Age: 24  company: JetBrains
# print_person("Bob", 41)  # Name: Bob  Age: 41  company: Microsoft
#
#
# # Неопределенное количество параметров
#
# def sum(*numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     print(f"sum = {result}")
#
# sum(1, 2, 3, 4, 5)
# sum(3 , 4, 5, 6)
#
# # Оператор return и возращение результата из функции
#
# def get_message():
#     return "Hello Metanit.com"
#
# # message = get_message()
# # print(message)
#
# print(get_message())

def double(number):
     return 2 * number
result1 = double(4)
result2 = double(5)

print(f"result1 = {result1}")
print(f"result2 = {result2}")

def sum(a, b):
    return a + b

result = sum(4, 6)
print(f"sum(4, 6) = {result}")
print(f"sum(3,5) = {sum(3, 5)}")

def print_person(name, age):
    if age > 120 or age < 1:
        print("Invalid age")
        return
    print(f"Name = {name} Age = {age}")

print_person("Tom", 22)














