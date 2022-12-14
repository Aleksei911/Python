# Файл как итератор
f = open('example.txt', 'r', encoding='UTF-8')
print(type(f))  # получаем тип нашей переменной
print('__next__' in f.__dir__())  # убеждаемся в том, что __next__ есть у нашего объекта
print(f.__next__())
print(f.__next__())
print(f.__next__())

"""
Как можно убедиться, исходя из вывода, мы получили первую строку нашего файла
При работе с файлами, использование файла как итератора не просто
позволяет перебирать файл построчно - в каждую итерацию загружена
только одна строка. Это очень важно при работе с большими
файлами на тысячи и сотни тысяч строк, например с лог-файлами. 
"""
