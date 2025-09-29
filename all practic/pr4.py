# name = input("Введите ваше имя: ")
# print(f"Привет, {name}")
# age = input(f"{name}, сколько тебе лет?\n")
# print(input())
from lesson3 import result

# number_1 = input("Введите певрое число: ")
# number_2 = input("Введите второе число: ")
#
# print("Операции с числами")
#
# print("Сложение:", float(number_1) + float(number_2))
# print("Вычитание:", float(number_1) - float(number_2))
# print("Умножение:", float(number_1) * float(number_2))
# print("Деление:", float(number_1) + float(number_2))


# p = input("Начальная сумма вклада: ")
# r = input("Процент по вкладу: ")
# t = input("Количество лет: ")
# print("Начисленные проценты:", (int(p) * int(r) * int(t)) / 100

# print("Функция как тип")
#
# def say_hello(): print("Hello")
# def say_goodbye(): print("Good Bye")
#
# message = say_hello
# message()  #Hello
# message2 = say_goodbye
# message2()  #Good Bye

# def sum(a, b): return a + b
# def multiply(a, b): return a * b
#
# operation = sum
# result = operation(5, 6)
# print(result)  #11
#
# operation = multiply
# print(operation(5, 6))
#
# print("Функция как параметр функции")
#
# def do_operation(a, b, operation):
#     result = operation(a,b)
#     print(f"result = {result}")
#
# def sum(a, b): return a + b
# def multiply(a, b): return a * b
#
# do_operation(5, 4, sum)
# do_operation(5, 4, multiply)

print("Функция как результат функции")

def sum(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b


def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply

operation = select_operation(1)
print(operation(10, 6))

operation = select_operation(2)
print(operation(10, 6))

operation = select_operation(3)
print(operation(10, 6))

print("Лямбда-выражение")

# lambda [параметры] : инструкция

message =  lambda: print("hello")

message() #hello

square = lambda n: n * n

print(square(4))
print(square(5))

sum = lambda a, b: a + b

print(sum(4, 5))
print(sum(5,6))

def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")

do_operation(5, 4, lambda a, b: a + b)
do_operation(5, 4, lambda a, b: a * b)


def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b


operation = select_operation(1)  # operation = sum
print(operation(10, 6))  # 16

operation = select_operation(2)  # operation = subtract
print(operation(10, 6))  # 4

operation = select_operation(3)  # operation = multiply
print(operation(10, 6))  # 60





