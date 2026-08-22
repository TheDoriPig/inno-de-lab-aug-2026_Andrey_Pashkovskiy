import random

random_number = random.randint(1, 20)
attempt = 1
attempt_left = 5
print("Я загадал число от 1 до 20. У тебя 5 попыток")
user_input = ""

while user_input != random_number:
    if attempt_left == 0:
        print(f"Игра окончена, осталось {attempt_left} попыток. Я загадал число {random_number}.")
        break

    user_input = int(input(f"Попытка {attempt}. Введите число: "))

    if user_input == random_number:
        print("Ты угадал! Отличная работа")
        break
    elif user_input > random_number:
        attempt_left -= 1
        attempt += 1
        print(f"Cлишком много! Осталось попыток: {attempt_left}\n")
    else:
        attempt_left -= 1
        attempt += 1
        print(f"Cлишком мало! Осталось попыток: {attempt_left}\n")
