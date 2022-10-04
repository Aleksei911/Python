# задание 1

# проверяем на дубликаты
numbers = [int(i) for i in input("Введите строку с числами: ").split()]

unique_numbers = set(numbers)
if len(unique_numbers) == len(numbers):
    print("В вашей последовательности дубликатов нет")
else:
    print("В вашей последовательности есть дубликаты!")

# задание 2

# создаем множество и неизменяемое множество, выполняем операции объединения и пересечения
numbers = {int(i) for i in input("Введите строку с числами: ").split()}
strings = frozenset([int(i) for i in input("Введите строку с числами: ").split()])
union_sets = numbers.union(strings)
intersection_sets = numbers.intersection(strings)

# DZ

# создаем кортеж с цифрами и считаем сумму
my_tuple = (1, 2, 3, 5, 8, 5, 6, 3, 9)
numbers_sum = sum(my_tuple)


# считаем количество повторений букв в кортеже

def chars_count(my_tuple):
    chars = set(my_tuple)
    for c in chars:
        print(f"{c}: {my_tuple.count(c)}")


long_word = ("т", "т", "а", "и", "и", "а", "и", "и", "и", "т",
             "т", "а", "и", "и", "и", "и", "и", "т", "и")

chars_count(long_word)


# расчет средней температуры

def meen_temp(my_tuple):
    print(f"Средняя температура: {int(sum(my_tuple) / len(my_tuple))} градусов")


week_temp = (26, 29, 34, 32, 28, 26, 23)
meen_temp(week_temp)
