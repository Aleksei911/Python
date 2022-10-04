from random import *

# задание 7

# запрашиваем стороны треугольника
num1 = int(input("Введите первую сторону треугольника: "))
num2 = int(input("Введите вторую сторону треугольника: "))
num3 = int(input("Введите третью сторону треугольника: "))

# создаем функцию-предикат, которая будет утверждать, существует треугольник с заданными сторонами или нет
is_triangle = num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2

# проверяем результат функции-предиката, и выводим соответствующее сообщение
if is_triangle:
    print("Такой треугольник существует")
else:
    print("Такой треугольник не существует")

# задание 10

# запрашиваем цвет доспехов и цвет щита
armor_color = input("Выберите цвет доспехов - red / yellow / black: ")
shild_color = input("Выберите цвет щита - red / yellow / black: ")

# создаем функцию-предикат, которая будет утверждать, соответствуют ли значения условию
is_set = armor_color != "red" and shild_color == "black"

# выводим результат функции-предиката
print(is_set)

# задача 1 (рулетка)

"""
Списки мы ещё не проходили, но на занятиях вы нам показывали как создаются списки и как обращаться к элементам
списка по индексу. этим и ограничимся =)
"""

colors = ["зеленое", "красное", "черное"]  # создаем список с цветами карманов рулетки
win_setup = randint(0, 36)  # иммитируем случайное попадание шарика в карман рулетки

# запрашиваем номер кармана рулетки
pocket = int(input("Введите номер кармана рулетки от 0 до 36: "))

if 0 <= pocket <= 36:  # проверяем есть ли введенное число на табло рулетки
    if pocket == 0:  # проверяем равно ли число нулю
        print(f"Ваш выбор {pocket} {colors[0]}!")  # если число равно нулю, цвет кармана зеленый
    elif (1 <= pocket <= 10 or 19 <= pocket <= 28) and pocket % 2 != 0:  # проверяем соответствует ли число условию
        print(f"Ваш выбор {pocket} {colors[1]}!")  # если число соответствует условию, цвет кармана красный
    elif (1 <= pocket <= 10 or 19 <= pocket <= 28) and pocket % 2 == 0:  # проверяем соответствует ли число условию
        print(f"Ваш выбор {pocket} {colors[2]}!")  # если число соответствует условию, цвет кармана черный
    elif (11 <= pocket <= 18 or 29 <= pocket <= 36) and pocket % 2 != 0:  # проверяем соответствует ли число условию
        print(f"Ваш выбор {pocket} {colors[2]}")  # если число соответствует условию, цвет кармана черный
    elif (11 <= pocket <= 18 or 29 <= pocket <= 36) and pocket % 2 == 0:  # проверяем соответствует ли число условию
        print(f"Ваш выбор {pocket} {colors[1]}!")  # если число соответствует условию, цвет кармана красный

    # проверяем какого цвета победный номер кармана рулетки + совпадаел ли с номером введенного кармана рулетки
    if win_setup == 0:
        if win_setup == pocket:
            print(f"Побеждает {win_setup} {colors[0]}! \nПоздравляем!!!")
        else:
            print(f"Побеждает {win_setup} {colors[0]}! \nПовезёт в следующий раз...")
    elif (1 <= win_setup <= 10 or 19 <= win_setup <= 28) and win_setup % 2 != 0:
        if win_setup == pocket:
            print(f"Побеждает {win_setup} {colors[1]}! \nПоздравляем!!!")
        else:
            print(f"Побеждает {win_setup} {colors[1]}! \nПовезёт в следующий раз...")
    elif (1 <= win_setup <= 10 or 19 <= win_setup <= 28) and win_setup % 2 == 0:
        if win_setup == pocket:
            print(f"Побеждает {win_setup} {colors[2]}! \nПоздравляем!!!")
        else:
            print(f"Побеждает {win_setup} {colors[2]}! \nПовезёт в следующий раз...")
    elif (11 <= win_setup <= 18 or 29 <= win_setup <= 36) and win_setup % 2 != 0:
        if win_setup == pocket:
            print(f"Побеждает {win_setup} {colors[2]}! \nПоздравляем!!!")
        else:
            print(f"Побеждает {win_setup} {colors[2]}! \nПовезёт в следующий раз...")
    elif (11 <= win_setup <= 18 or 29 <= win_setup <= 36) and win_setup % 2 == 0:
        if win_setup == pocket:
            print(f"Побеждает {win_setup} {colors[1]}! \nПоздравляем!!!")
        else:
            print(f"Побеждает {win_setup} {colors[1]}! \nПовезёт в следующий раз...")
else:
    print("Ошибка! Должно быть число от 0 до 36")  # выводим сообщение о несоответствии числа условию

# задача 2

# запрашиваем ввод данных
day = int(input("Введите день своего рождения: "))
month = input("Введите месяц своего рождения: ")

# в зависимости от введённых даты и месяцы выводим знак зодиака
if (21 <= day <= 31 and month.lower() == "март") or (1 <= day <= 20 and month.lower() == "апрель"):
    print("Ваш знак зодиака - ОВЕН")
elif (21 <= day <= 30 and month.lower() == "апрель") or (1 <= day <= 21 and month.lower() == "май"):
    print("Ваш знак зодиака - ТЕЛЕЦ")
elif (22 <= day <= 31 and month.lower() == "май") or (1 <= day <= 21 and month.lower() == "июнь"):
    print("Ваш знак зодиака - БЛИЗНЕЦЫ")
elif (22 <= day <= 30 and month.lower() == "июнь") or (1 <= day <= 22 and month.lower() == "июль"):
    print("Ваш знак зодиака - РАК")
elif (23 <= day <= 31 and month.lower() == "июль") or (1 <= day <= 21 and month.lower() == "август"):
    print("Ваш знак зодиака - ЛЕВ")
elif (22 <= day <= 31 and month.lower() == "август") or (1 <= day <= 23 and month.lower() == "сентябрь"):
    print("Ваш знак зодиака - ДЕВА")
elif (24 <= day <= 30 and month.lower() == "сентябрь") or (1 <= day <= 23 and month.lower() == "октябрь"):
    print("Ваш знак зодиака - ВЕСЫ")
elif (24 <= day <= 31 and month.lower() == "октябрь") or (1 <= day <= 22 and month.lower() == "ноябрь"):
    print("Ваш знак зодиака - СКОРПИОН")
elif (23 <= day <= 30 and month.lower() == "ноябрь") or (1 <= day <= 22 and month.lower() == "декабрь"):
    print("Ваш знак зодиака - СТРЕЛЕЦ")
elif (23 <= day <= 31 and month.lower() == "декабрь") or (1 <= day <= 20 and month.lower() == "январь"):
    print("Ваш знак зодиака - КОЗЕРОГ")
elif (21 <= day <= 31 and month.lower() == "январь") or (1 <= day <= 19 and month.lower() == "февраль"):
    print("Ваш знак зодиака - ВОДОЛЕЙ")
elif (20 <= day <= 29 and month.lower() == "февраль") or (1 <= day <= 20 and month.lower() == "март"):
    print("Ваш знак зодиака - РЫБЫ")
else:
    print("Проверьте корректность вводимых данных")

# задача 3

# играем с компьютером в камень, ножницы, бумага, ящерица, спок =)

# создаем список вариантов выбора значений для компьютера
values = ["камень", "ножницы", "бумага", "ящерица", "спок"]

# компьютер делает рандомный выбор
computer_value = values[randint(0, 4)]

# просим пользователя сделать свой выбор
player_value = input("Выберите значение (камень, ножницы, бумага, ящерица, спок): ")

# сравниваем значения и выводим результат
if player_value.lower() in values:
    if computer_value == "камень":
        if player_value.lower() == "ящерица":
            print("Камень давит ящерицу... \nВы проиграли =(")
        elif player_value.lower() == "ножницы":
            print("Камень затупляет ножницы... \nВы проиграли =(")
        elif player_value.lower() == "спок":
            print("Спок превращает камень в пар... \nВы выиграли =)")
        elif player_value.lower() == "бумага":
            print("Бумага оборачивает камень... \nВы выиграли =)")
    elif computer_value == "ящерица":
        if player_value.lower() == "спок":
            print("Ящерица отравляет спока... \nВы проиграли =(")
        elif player_value.lower() == "бумага":
            print("Ящерица съедает бумагу... \nВы проиграли =(")
        elif player_value.lower() == "ножницы":
            print("Ножницы отрезают голову ящерице... \nВы выиграли =)")
        elif player_value.lower() == "камень":
            print("Камень давит ящерицу... \nВы выиграли =)")
    elif computer_value == "спок":
        if player_value.lower() == "ножницы":
            print("Спок ломает ножницы... \nВы проиграли =(")
        elif player_value.lower() == "камень":
            print("Спок превращает камень в пар... \nВы проиграли =(")
        elif player_value.lower() == "бумага":
            print("Бумага опровергает спока... \nВы выиграли =)")
        elif player_value.lower() == "ящерица":
            print("Ящерица отравляет спока... \nВы выиграли =)")
    elif computer_value == "ножницы":
        if player_value.lower() == "бумага":
            print("Ножницы режут бумагу... \nВы проиграли =(")
        elif player_value.lower() == "ящерица":
            print("Ножницы отрезают голову ящерице... \nВы проиграли =(")
        elif player_value.lower() == "спок":
            print("Спок ломает ножницы... \nВы выиграли =)")
        elif player_value.lower() == "камень":
            print("Камень затупляет ножницы... \nВы выиграли =)")
    elif computer_value == "бумага":
        if player_value.lower() == "камень":
            print("Бумага оборачивает камень... \nВы проиграли =(")
        elif player_value.lower() == "спок":
            print("Бумага опровергает спока... \nВы проиграли =(")
        elif player_value.lower() == "ножницы":
            print("Ножницы режут бумагу... \nВы выиграли =)")
        elif player_value.lower() == "ящерица":
            print("Ящерица съедает бумагу... \nВы выиграли =)")
else:
    print("Некорректный ввод данных!")
