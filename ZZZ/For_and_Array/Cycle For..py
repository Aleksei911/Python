"""
Вступление:
Приступаем к изучению цикла for
первое, что необходимо усвоить, это то, что
цикл for является циклом с параметром
"""

for elem in range(10):  # для элементов в последовательности range(10)
    print(elem)  # выведи в терминал значение элемента

"""
Обратим внимание на строение цикла for. 
Для объявления такого цикла необходимо:
1. Сперва указать зарезервированное слово - for - 
2. Далее необходимо указать название временной переменной
при этом название данной переменной может быть любым.
В идеале необходимо указывать названия, которые будут нести некоторую
смысловую нагрузку, т.е.
for abrakadabra in [1, 2, 3, 4]:  - нежелательно
    print (abrakadabra) 

for object in [1, 2, 3, 4]: - рекомендуется
    print(object) 
3. Необходимо указать оператор - in - 
4. После чего указать итерируемый объект (прим. список, строку, словарь и т.д.)
"""

# Партия 1. Range(x)
"""
Здесь необходимо разобраться в том, что же такое range(x).
range() - это встроенная функция Python, 
которая возвращает итерируемый объект ( range object ), 
содержащий целые числа.
Простыми словами range() создает последовательность целых чисел в заданном промежутке.
Также как и срезы range(start, end, step) поддерживает три параметра.
start - начало последовательности
end - конец последовательности
step - шаг, с которым будет создана последовательность.
"""

# ПАРТИЯ 2. Работа в цикле со строками.
example_string = 'Fill is coming'
for elem in example_string:
    """
    Теперь вспомним, что пройденные нами строки str()
    являются итерируемыми объектами, т.е. по ним с помощью
    цикла (циклов) можно произвести нужное нам количество итераций
    """
    print(elem, end='\n')


"""
Вывод:
> F
> i
> l
> l
Обратите внимание на следующий момент.
Итерация по строкам происходит не по отдельным словам (или предложениям).
Цикл проходит по строке посимвольно, т.е.
для цикла наша переменная elem 
будет принимать значения символов из итерируемой строки (или объекта)
"""
