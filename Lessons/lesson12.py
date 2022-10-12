import math
import random


# задание 1

def counter(num):
    if num // 10 != 0:
        return 1 + counter(num // 10)
    else:
        return 1


print(counter(10000))


# задание 2

def square_circle(r):
    return math.pi * r ** 2


def square_rectangle(a, b):
    return a * b


def square_triangle(a, b, c):
    p = (a + b + c) / 2
    h = (2 * (p * (p - a) * (p - b) * (p - c)) ** 0.5) / a
    return 0.5 * a * h


choice = input('площадь какой фигуры нужно вычислить? (круг, прямоугольник, треугольник): ')

if choice == 'круг':
    square_circle(int(input('Введите радиус: ')))
elif choice == 'прямоугольник':
    square_rectangle(int(input('Введите сторону a: ')),
                     int(input('Введите сторону b: ')))
elif choice == 'треугольник':
    square_triangle(int(input('Введите сторону a: ')),
                    int(input('Введите сторону b: ')),
                    int(input('Введите сторону c: ')))


# задание 3

def numbers(a, b):
    my_list = [random.randint(a, b) for _ in range(10)]


numbers(int(input('Введите нижний предел диапазона: ')),
        int(input('Введите верхний предел диапазона: ')))

