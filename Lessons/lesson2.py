import math
import random

a = 6
b = 2

multi = a * b  # умножаем а на b
delenie = a / b  # делим а на b
stepen = a ** b  # возводим а в степень b
cd = a // b  # делим на цело a на b
ostatok = a % b  # вычисляем остаток от деления a на b

# задание 1
num1 = int(input())
num2 = int(input())
num3 = int(input())

# умножаем
mult1 = num1 * num2
mult2 = num1 * num3
mult3 = num2 * num3

# делим
del1 = num1 / num2
del2 = num1 / num3
del3 = num2 / num3
del4 = num3 / num2
del5 = num3 / num1

# возводим в степень
step1 = num1 ** num2
step2 = num1 ** num3
step3 = num2 ** num3
step4 = num3 ** num2
step5 = num3 ** num1

# делим без остатка
sd1 = num1 // num2
sd2 = num1 // num3
sd3 = num2 // num3
sd4 = num3 // num2
sd5 = num3 // num1

# находим остаток от деления
ost1 = num1 // num2
ost2 = num1 // num3
ost3 = num2 // num3
ost4 = num3 // num2
ost5 = num3 // num1

# задача 2
print(17 / 2 * 3 + 2,
      2 + 17 / 2 * 3,
      19 % 4 + 15 / 2 * 3,
      (15 + 6) - 10 * 4,
      17 / 2 % 2 * 3 ** 3)

# задача 3
money = 11
prise = 1.5
count = 3
print(money - prise * count)

# задание 4
print((30 + 33 + 24 + 28 + 31 + 33 + 38 + 29 + 22 + 31 + 28 + 15 + 32 + 29 + 21 + 41 + 49) / 17)

# задача 5
grad = float(input("Введите угол в градусах: "))
print("угол ", grad, " градусов равняется ", math.radians(grad), " радиан")

# задача 6
a, b, c = int(input()), int(input()), int(input())
d = b ** 2 - 4 * a * c

# задача 7
num = int(input())
sum = num // 100 + num // 10 % 10 + num % 10

# задача 8
a = int(input("Введите катет 1: "))
b = int(input("Введите катет 2: "))
c = int(input("Ведите гипотенузу: "))
square = a * b / 2
perimeter = a + b + c
