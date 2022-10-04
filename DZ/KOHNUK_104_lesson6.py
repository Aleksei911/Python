from random import *

# задание 4

first_number, second_number = int(input("Введите первое число: ")), int(input("Введите второе число: "))

if first_number < 0 or second_number < 0:  # проверяем есть ли вообще отрицательные числа
    # если первое меньше второго + < 0 а второе >= 0, выводим отрицательные числа двигаясь от первого числа до нуля
    if first_number < second_number and second_number >= 0:
        while first_number < second_number:
            first_number += 1
            if first_number == 0:
                break
            print(first_number, end=" ")
    # если первое меньше второго + < 0 и второе < 0, выводим отрицательные числа двигаясь от первого числа ко второму
    elif first_number < second_number:
        while first_number < second_number:
            first_number += 1
            if first_number == second_number:
                break
            print(first_number, end=" ")
    # если первое больше второго + >= 0 а второе < 0, выводим отрицательные числа двигаясь от нуля до первого числа
    elif first_number > second_number and first_number >= 0:
        first_number = 0
        while first_number > second_number:
            first_number -= 1
            if first_number == second_number:
                break
            print(first_number, end=" ")
    # если первое больше второго + < 0 и второе < 0, выводим отрицательные числа двигаясь от второго числа к первому
    elif first_number > second_number:
        while first_number > second_number:
            first_number -= 1
            if first_number == second_number:
                break
            print(first_number, end=" ")
else:
    print("Отрицательных чисел нет!")

# задание 6

print("""
      *** Вас приветствует простейший калькулятор! ***
      """)
while True:
    print("""Выберите нужную Вам операцию:
             1. для операции сложения наберите 1
             2. для операции вычитания наберите 2
             3. для операции умножения наберите 3
             4. для операции деления наберите 4
             5. для выхода из программы наберите 0
             """)
    action = int(input("Ваш выбор: "))
    if action < 0 or action > 4:
        print("\nНеверно введён номер!\n")
        continue
    if action == 0:
        break
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    if action == 4 and second_number == 0:
        print("\nНа ноль делить нельзя!", end="\n\n")
        continue
    if action == 1:
        print(f"\n{first_number} + {second_number} = {first_number + second_number}", end="\n\n")
    elif action == 2:
        print(f"\n{first_number} - {second_number} = {first_number - second_number}", end="\n\n")
    elif action == 3:
        print(f"\n{first_number} * {second_number} = {first_number * second_number}", end="\n\n")
    elif action == 4:
        print(f"\n{first_number} / {second_number} = {first_number / second_number}", end="\n\n")

# задание 7

# создаем массив из 7 цифр (чисел)
numbers = [int(i) for i in input("Введите 7 цифр (чисел) через пробел: ").split()]

even_count = 0
uneven_count = 0
step = 0
# проходимся по массиву и подсчитываем количество четных и нечетных чисел
while step < len(numbers):
    if numbers[step] % 2 == 0:
        even_count += 1
    else:
        uneven_count += 1
    step += 1
# по завершении цикла сравниваем результаты и выводим соответствующее значение
else:
    if even_count > uneven_count:
        print(sum(numbers))
    else:
        print(numbers[0] * numbers[2] * numbers[5])

# DZ

print("          ***** Блекджек *****          ")
deck = ["двойка", "тройка", "четвёрка", "пятерка", "шестерка", "семерка", "восьмерка",
        "девятка", "десятка", "валет", "дама", "король", "туз"]
player_cards = []  # записываем карты игрока
player_sum = 0  # записываем сумму очков игрока
computer_cards = []  # записываем карты крупье
computer_sum = 0  # записываем сумму очков крупье
player_flag = True
computer_flag = True
while player_flag:
    player_index = randint(1, 12)
    player_cards.append(deck[player_index])  # добавляем рандомную карту игроку и подсчитываем очки
    if 0 <= player_index <= 8:
        player_sum += (player_index + 2)
    elif 9 <= player_index <= 11:
        player_sum += 10
    else:
        tuz = int(input("Вам выпал ТУЗ! Выберите значение 1 или 11: "))
        player_sum += tuz
    if player_sum > 21:  # если сумма больше 21 - игрок автоматом проиграл
        print(f"Сумма ваших очков составляет - {player_sum}. Вы проиграли!")
        computer_flag = False
        break
    elif player_sum == 21 and len(player_cards) == 2:  # если у игрока туз + 10 очков - Блекджек
        print("  ***** Блекджек *****.   Вы выиграли!!!")
        computer_flag = False
        break
    print("У вас на руках:", *player_cards)  # информируем игрока о его очках и спрашиваем давать ли ещё карту
    print(f"Сумма ваших очков составляет - {player_sum}")
    player_step = input("Тянуть ещё карту? Y/N: ")
    if player_step.upper() == "N":
        player_flag = False
while computer_flag:
    computer_index = randint(1, 12)  # добавляем рандомную карту крупье и подсчитываем очки
    computer_cards.append(deck[computer_index])
    if 0 <= computer_index <= 8:
        computer_sum += (computer_index + 2)
    elif 9 <= computer_index <= 11:
        computer_sum += 10
    else:
        if computer_sum + 11 <= 21:
            computer_sum += 11
        else:
            computer_sum += 1
    # крупье тянет до тех пор, пока не превысит очки игрока или пока не будет 21 + сравниваем результаты
    if computer_sum > player_sum or computer_sum == 21:
        if computer_sum > 21:
            print(f"Сумма очков крупье составляет - {computer_sum}")
            print("Вы выиграли!!!")
            break
        elif computer_sum == player_sum:
            print(f"Сумма очков крупье составляет - {computer_sum}")
            print("НИЧЬЯ!")
            break
        else:
            print(f"Сумма очков крупье составляет - {computer_sum}")
            print("Вы проиграли!")
            break
