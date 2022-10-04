from random import *

# задание 1 (вычисляем гиппотенузу)

hippo = lambda x, y: (x ** 2 + y ** 2) ** 0.5

total = hippo(int(input("Введите 1 катет: ")), int(input("Введите 2 катет: ")))


# задание 2 (находим среднее число)

def midle(num1, num2, num3):
    if num1 < num2 < num3 or num3 < num2 < num1:
        return num2
    elif num2 < num1 < num3 or num3 < num1 < num2:
        return num1
    elif num2 < num3 < num1 or num1 < num3 < num2:
        return num3
    else:
        print("Среднего числа нет!")


num1, num2, num3 = int(input("Введите 1 число: ")), \
                   int(input("Введите 2 число: ")), \
                   int(input("Введите 3 число: "))
total = midle(num1, num2, num3)


# задание 3 (находим нечетное из двух чисел)

def uneven(num1, num2):
    if num1 % 2 == 0 and num2 % 2 != 0:
        print(f"Число {num2} является нечетным!")
    elif num1 % 2 != 0 and num2 % 2 == 0:
        print(f"Число {num1} является нечетным!")
    elif num1 % 2 == 0 and num2 % 2 == 0:
        print("Оба числа являются четными!")
    else:
        print("Оба числа являются нечетными!")


num1 = int(input("Введите 1 число: "))
num2 = int(input("Введите 2 число: "))
uneven(num1, num2)


# задание 4 (переворачиваем введенное число)

def reversed_number(num):
    print(int(str(num)[::-1]))


number = int(input("Введите число: "))
reversed_number(number)


# задание 5 (выводим на экран прямоугольник)

def rectangle(width, height):
    count = 0
    while count <= height:
        if count == 0 or count == height:
            print("*" * width)
        else:
            print("*" + "-" * (width - 2) + "*")
        count += 1


rectangle_width = int(input("Введите ширину прямоугольника: "))
rectangle_height = int(input("Введите высоту прямоугольника: "))

rectangle(rectangle_width, rectangle_height)


# задание 6 (находим совершенные числа)

def perfect_numbers(length):
    total = []
    summa = 0
    for i in range(2, length):
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                summa += j
        if summa == i:
            total.append(i)
        summa = 0
    print(*total)


number = int(input("До какого числа найти совершенные числа?: "))
perfect_numbers(number)

# задание 7 (заполняем массив числами (кроме последнего. его мы выводим на экран). затем добавляем ещё число по индексу)

numbers = []
for i in range(10):
    temp = int(input("Введите число: "))
    if i < 9:
        numbers.append(temp)
    else:
        print(temp)
number = int(input("Введите ещё 1 значение: "))
index = int(input("на какую позицию в списке (от 0 до 10) поместить ваше значение: "))
numbers.insert(index - 1, number)
print(numbers)


# задание 8 (считаем количество слов в строке)

def word_counter(string):
    return len(string.split())


total = word_counter(input("Введите строку: "))


# задание 9 (убираем заглавные буквы из строки)

def lower_string(string):
    new_string = ""
    for c in string:
        if not c.isupper():
            new_string += c
    print(new_string)


lower_string(input("Введите строку текста: "))


# задание 10 (выводим числа на экран, пропуская кратные 7)

def seven_will_not_pass(num=100):
    for i in range(num + 1):
        if i % 7 == 0:
            continue
        else:
            print(i, end=" ")


seven_will_not_pass()

# задание 11 (выводим сумму чисел от 1 до 100)

print(sum(range(1, 100)))


# задание 12 (выводим факториал числа)

def my_factorial(num):
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total


number = int(input("Факториал какого числа нужно найти?: "))
print(f"Факториал числа {number} = {my_factorial(number)}")


# задание 13 (выводим последовательность чисел "ёлочкой")

def fir(num):
    string_count = 1
    step = 2
    for i in range(1, num + 1):
        print(i, end=" ")
        if i == string_count:
            print()
            string_count += step
            step += 1


fir(int(input("Ведите число: ")))


# задание 14 (печатаем все целые степени двойки не превосходящие число, в порядке возрастания)

def powers_of_two(num):
    temp = 1
    count = 1
    while temp < num:
        print(temp, end=" ")
        temp = 2 ** count
        count += 1


powers_of_two(int(input("Введите число: ")))
