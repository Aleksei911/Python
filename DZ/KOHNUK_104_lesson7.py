from random import *


# задание 3

# создаем функцию, которая будет возвращать кортеж значений периметра, прощади и диагонали квадрата
def square(length):
    return 4 * length, length ** 2, length * 2 ** 0.5


print(square(int(input("Введите сторону квадрата: "))))


# задание 4

# создаем функцию, которая будет возвращать строку (время года) в зависимости от месяца
def season(num):
    if 1 <= num <= 2 or num == 12:
        return "Зима"
    elif 3 <= num <= 5:
        return "Весна"
    elif 6 <= num <= 8:
        return "Лето"
    elif 9 <= num <= 11:
        return "Осень"
    else:
        return "Некорректные данные!"


print(season(int(input("Для получения времени года, введите порядковый номер месяца: "))))


# задание 5

# создаем функцию, которая будет возвращать True если число простое и False в противном случае
def is_prime(num):
    if 0 <= num <= 3:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


print(is_prime(int(input("Вводите число от 0 до 1000: "))))


# задание 6

# создаем функцию, которая будет возвращать среднее арифметическое элементов массива
def middle(some_list):
    return sum(some_list) / len(some_list)


# создаем список и заполняем его случайными числами
numbers = [randint(1, 1000) for _ in range(10)]

print(f"среднее арифметическое элементов массива {numbers} = {middle(numbers)}")

# DZ

symbol = input("""
                  ***** Вас приветствует простейший калькулятор! *****
                  
Выберите действие:
1. Для операции сложения выберите "+"
2. Для операции вычитания выберите "-"
3. Для операции умножения выберите "*"
4. Для операции деления выберите "/"
Ваш выбор: """)
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
summa = lambda x, y: x + y
difference = lambda x, y: x - y
multi = lambda x, y: x * y
division = lambda x, y: x / y

if symbol == "+":
    print(f"{num1} + {num2} = {summa(num1, num2)}")
elif symbol == "-":
    print(f"{num1} - {num2} = {difference(num1, num2)}")
elif symbol == "*":
    print(f"{num1} * {num2} = {multi(num1, num2)}")
elif symbol == "/":
    print(f"{num1} / {num2} = {division(num1, num2)}")
else:
    print("Некорректные данные!")
