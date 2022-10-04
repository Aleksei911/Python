import random

# задание 1

num = int(input("Введите целое число: "))

if num % 2 == 0:
    print(f"Число {num} - четное!")
else:
    print(f"Число {num} - нечетное!")


# задание 2

finger = int(input("Введите порядковый номер пальца: "))

if finger == 1:
    print(f"Палец под номером {finger} - большой!")
elif finger == 2:
    print(f"Палец под номером {finger} - указательный!")
elif finger == 3:
    print(f"Палец под номером {finger} - средний!")
elif finger == 4:
    print(f"Палец под номером {finger} - безымянный!")
elif finger == 5:
    print(f"Палец под номером {finger} - мизинец!")
else:
    print("Если вы не из Чернобыля, то пальцев должно быть не больше пяти =)")


# задание 3

month = int(input("Введите номер месяца: "))
if 1 <= month <= 2 or month == 12:
    print("Зима")
elif 3 <= month <= 5:
    print("Весна")
elif 6 <= month <= 8:
    print("Лето")
elif 9 <= month <= 11:
    print("Осень")
else:
    print("Загляни в календарь!")


# задание 4

one = int(input())
two = int(input())
three = int(input())

if one > two and one > three:
    print(f"{one} is biggest")
elif two > one and two > three:
    print(f"{two} is biggest")
elif three > one and three > two:
    print(f"{three} is biggest")


# задание 5

first_player = random.randint(1, 3)
second_player = random.randint(1, 3)

if first_player == 1:
    if second_player == 2:
        print("Камень побеждает Ножницы")
    elif second_player == 3:
        print("Бумага побеждает Камень")
    elif second_player == 1:
        print("Ничья")
elif first_player == 2:
    if second_player == 2:
        print("Ничья")
    elif second_player == 3:
        print("Ножницы побеждают Бумагу")
    elif second_player == 1:
        print("Камень побеждает Ножницы")
elif first_player == 3:
    if second_player == 2:
        print("Ножницы побеждают Бумагу")
    elif second_player == 3:
        print("Ничья")
    elif second_player == 1:
        print("Бумага побеждает Камень")


# задание 6

num1 = int(input())
num2 = int(input())
flag = num1 > num2
if flag:
    print("YES")
else:
    print("NO")


# задание 7

num1 = int(input())
num2 = int(input())
num3 = int(input())
is_triangle = num1 > num2 + num3 and num2 > num1 + num3 and num3 > num1 + num2

if is_triangle:
    print("Такой треугольник существует")
else:
    print("Такой треугольник не существует")


# задание 8

num1 = float(input("Введите число: "))
sign = input("Введите знак операции (+, -, /, *): ")
num2 = float(input("Введите число: "))

if sign == "+":
    print(num1 + num2)
elif sign == "-":
    print(num1 - num2)
elif sign == "*":
    print(num1 * num2)
elif sign == "/":
    print(num1 / num2)


# задание 9

st = input("Введите слово: ")
is_mister = st == "Mister"

if is_mister:
    print("Введено слово Mister")
else:
    print("Введено слово отличное от слова Mister")