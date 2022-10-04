from random import *

# задание 1

temp = [randint(1, 100) for _ in range(10)]

total = tuple(temp)

print(min(total), max(total))

# задание 2

temp1 = tuple([randint(0, 5) for _ in range(10)])
temp2 = tuple([randint(-5, 0) for _ in range(10)])
total = temp1 + temp2

print(f"Итоговый кортеж: {total}",
      f"Количество нулей в нем = {total.count(0)}", sep="\n")

# задание 3

strings = tuple([s for s in input("Введите струку текста: ").split()])
print(*strings, sep=", ")

# задание 4

a = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
b = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)

if sum(a) > sum(b):
    print(f"Сумма больше в кортеже - {a}")
else:
    print(f"Сумма больше в кортеже - {b}")

print(f"Порядковый номер минимального объекта в кортеже А - {a.index(min(a)) + 1}",
      f"Порядковый номер минимального объекта в кортеже B - {b.index(min(b)) + 1}", sep="\n")
