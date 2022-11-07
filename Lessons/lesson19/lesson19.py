from datetime import datetime

"""
Теперь давайте создадим функцию, которая с помощью
цикла for заполнит пустой список четными числами
от 0 до 10  5
"""


def count_the_time(func):  # создаем декоратор
    # параметр func - функция которую мы будем оборачивать
    # return возвращает результат работы функции wraper
    def wrapper():  # создаем вложенную функцию-обертку
        start = datetime.now()  # отмечаем старт отсчета
        result = func()  # вызываем функцию, которая придет в качестве аргумента в count_the_time(func)
        print(datetime.now() - start)  # отмечаем время работы
        return result  # возвращаем результат переданной функции, т.е. то что функция должна была вернуть

    return wrapper  # возвращаем то что вернула функция wraper


@count_the_time  # вызов декоратора для функции
def create_list():
    list_ = []  # целевой код
    for _ in range(10 ** 5):  # целевой код
        if _ % 2 == 0:  # целевой код
            list_.append(_)  # целевой код
    return list_


@count_the_time  # вызов декоратора для функции
def create_list_gen():
    list_ = [i for i in range(10 ** 5) if i % 2 == 0]  # целевой код
    return list_


ex1 = create_list()
ex2 = create_list_gen()

############################################

def decorator(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print(count)
        return func()

    return wrapper


@decorator
def some_func():
    print('something')


some_func()
some_func()
some_func()
some_func()
