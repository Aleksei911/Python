from fractions import Fraction


# Задача 1

def BMI(weight: int, height: int) -> float:
    bmi = weight / ((height / 100) ** 2)

    if bmi <= 16:
        print(f"BMI = {bmi}",
              "\nВыраженный дефицит массы тела")
        return bmi
    elif 16 < bmi <= 18.5:
        print(f"BMI = {bmi}",
              "\nНедостаточная (дефицит) масса тела")
        return bmi
    elif 18.5 < bmi <= 25:
        print(f"BMI = {bmi}",
              "\nНорма")
        return bmi
    elif 25 < bmi <= 30:
        print(f"BMI = {bmi}",
              "\nИзбыточная масса тела (предожирение)")
        return bmi
    elif 30 < bmi <= 35:
        print(f"BMI = {bmi}",
              "\nОжирение первой степени")
        return bmi
    elif 35 < bmi <= 40:
        print(f"BMI = {bmi}",
              "\nОжирение второй степени")
        return bmi
    elif bmi > 40:
        print(f"BMI = {bmi}",
              "\nОжирение третьей степени (морбидное)")
        return bmi


BMI(int(input("Введите ваш вес: ")), int(input("Введите ваш рост: ")))


# Задача 2

def figure(*args) -> None:
    if 3 <= len(args) <= 4:
        print(f"{len(args)}-х угольник")
    elif 5 <= len(args) <= 10:
        print(f"{len(args)}-и угольник")
    else:
        print("Некорректное значение")


# Задача 4

def money(quantity: int) -> None:
    print(f"Стоимость доставки для {quantity} товаров составит {10.95 + (quantity - 1) * 2.95} долларов")


money(int(input("Введите кол-во заказов: ")))


# Задача 5

def reduction(a: int, b: int) -> tuple:
    total = Fraction(a, b)
    return total.numerator, total.denominator


numerator = int(input("Введите числитель дроби: "))
denominator = int(input("Введите знаменатель дроби: "))
print(reduction(numerator, denominator))


# Задача 6

def func_for_list(any_list: list) -> None:
    print(any_list[::-1])
    print(sorted(any_list, key=str))
    print(sorted(any_list, key=str, reverse=True))
    print(any_list[1:7])
    print(any_list[:4] + any_list[5:])
    print(list(set(any_list)))
    print([i for i in any_list if type(i) is not int])


lst = [1, 44, "hjj", 1, "yuyt", "uuuy", 455, 15, "wqe", 15]
func_for_list(lst)


# Задача 7

def countRange(any_list: list, a: int, b: int) -> int:
    return len([num for num in any_list if a <= num < b])


start = 7
stop = 25
list1 = [1, 5, 16, 35, 8, 19, 30, 21]
list2 = [2, 6.5, 9, 49, 11.8, 4.3, 15, 37]
print(countRange(list1, start, stop))
print(countRange(list2, start, stop))


# Задача 8

def search_lists(any_list: list) -> int:
    return len([elem for elem in any_list if type(elem) == list])


# Задача 9

def is_anagram(a: str, b: str) -> None:
    if set(a) == set(b) and len(a) == len(b):
        print(f"Слова {a} и {b} являются анаграммами")
    else:
        print(f"Слова {a} и {b} не являются анаграммами")


word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")
is_anagram(word1, word2)


# Задача 10

def message(any_string: str) -> str:
    total = ""
    phone = {
        1: ".,?!:",
        2: "ABC",
        3: "DEF",
        4: "GHI",
        5: "JKL",
        6: "MNO",
        7: "PQRS",
        8: "TUV",
        9: "WXYZ",
        0: " "
    }
    for c in any_string.upper():
        for key, value in phone.items():
            if c in value:
                total += str(key) * (value.index(c) + 1)

    return total


print(message(input("Please, enter your message: ")))


# Задача 11

def arrow(any_list: list) -> list:
    if len(any_list) == 0:
        return []
    if type(any_list[0]) != list:
        total = [any_list[0]]
        temp = any_list[1:]
        return total + arrow(temp)
    if type(any_list[0]) == list:
        total = any_list[0]
        temp = any_list[1:]
        return arrow(total) + arrow(temp)


example = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
print(arrow(example))


# Задача 3

def dates(year: int, month: str, day: int):
    days = {"января": range(1, 32),
            "февраля": range(1, 29),
            "марта": range(1, 32),
            "апреля": range(1, 31),
            "мая": range(1, 32),
            "июня": range(1, 31),
            "июля": range(1, 32),
            "августа": range(1, 32),
            "сентября": range(1, 31),
            "октября": range(1, 32),
            "ноября": range(1, 31),
            "декабря": range(1, 32)}
    months = list(days.keys())
    if month.lower() == "декабрь" and day == 31:
        print(f"1 января {year + 1}")
    elif day == days[month.lower()][-1]:
        print(f"1 {months[months.index(month) + 1]} {year}")
    else:
        print(f"{day + 1} {month} {year}")


dates(2022, "апреля", 30)
