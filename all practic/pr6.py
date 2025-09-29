# password = "qwerty123"
# a = input("Введите пароль: ")
#
# if password == a:
#     print("Введен верный пароль!")
# else:
#     print("Введен неверный пароль!")

# number = 1
# while number < 10 :
#     result = 6 * number
#     print(f"6 * {number} =", result)
#     number += 1
# print("Таблица умножения на 6 завершена!")

# num = int(input("Введите число: "))
# number = 1
# while number <= num:
#     print(f"{number} + {number} =", number + number)
#     number += 1
# print("Работа программы завершена!")

import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempt_count = 0
    print("Hello! I've picked a number between 1 and 100. Try to guess it!")

    while True:
        user_input = input("Enter your guess: ")

        if not user_input.isdigit():
            print("Error: please enter a valid whole number.")
            continue

        guess = int(user_input)
        attempt_count += 1

        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempt_count} attempts.")
            break

# Start the game
guess_the_number()