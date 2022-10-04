from array import array

# импортируем из модуля array метод array
# при import array
# конструкция будет выглядеть как array.array(typecode, object)

s = array('f', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# создание массива с указанием float в качестве тайпкода
# и генератора списков в качестве объекта

for elem in s:
    print(elem)
print(s)  # здесь мы выведем array-object
print(type(s))  # узнаем его тип
print(list(s))  # здесь же приведем к стандартому list
print(list(s) == s)  # сравним array с list Вывод: False
