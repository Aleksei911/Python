a = 1
"""
Итератор - любой объект, обладающий методом __next__. Этот метод
возвращает следующий элемент, если он есть, в противном случае
он возвращает исключение StopIteration, т.е. в момент когда элементы закончились
"""

# пример создания итератора из списка
elems = [1, 2, 3]
iter_list = iter(elems)
print(next(iter_list))  # >>> 1
print(next(iter_list))  # >>> 2
print(next(iter_list))  # >>> 3
print(next(iter_list))    # >>> StopIteration

"""
После того, как закончились все элементы, возвращается 
исключение StopIteration
"""