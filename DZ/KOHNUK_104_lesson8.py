# задание 4

# функция проходит по элементам первого списка и проверяет, есть ли такие объекты во втором списке
# если есть - добавляет этот элемент в результирующий список. в завершении возвращает результирующий список
def duplicate_objects(list1, list2):
    result = []
    for elem in list1:
        if elem in list2:
            result.append(elem)
    return result


a = [5, [1, 2], 2, 'r', 4, 'ee']
b = [4, 'we', 'ee', 3, [1, 2]]

duplicate_objects(a, b)


# задание 5

# функция объединяет 2 списка и возвращает результат их сложения
def sum_of_lists(list1, list2):
    return list1 + list2


# функция добавляет объект 6 по индексу 3
def add_six(my_list):
    my_list.insert(3, 6)


# функция удаляет все строчные объекты из списка и возвращает результирующий список
def dell_text(my_list):
    for elem in my_list:
        if type(elem) == str:
            del my_list[my_list.index(elem)]
    return my_list


a = [4, 6, 'py', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]

full_list = sum_of_lists(a, b)
add_six(full_list)
dell_text(full_list)
count = len(full_list)


# DZ

# функция проходит по элементам списка. если элемент является объектом типа Integer, проверяет его на четность
# если число четное - находит сумму его цифр. если нет - заменяет его значение в списке на 1
def numbers(my_list):
    for elem in my_list:
        if type(elem) == int:
            if elem % 2 == 0:
                temp = 0
                for c in str(elem):
                    temp += int(c)
                print(f"Число {elem} является четным! сумма его цифр равна {temp}")
            else:
                my_list[my_list.index(elem)] = 1
                print(f"Число {elem} успешно заменено на 1, т.к. является нечетным!")


# функция проходит по элементам списка. если элемент является объектом типа String, проходим по символам строки
# и подсчитываем количество гласных и согласных букв
def chars(my_list):
    for elem in my_list:
        if type(elem) == str:
            vowels = 0
            consonants = 0
            for c in elem.strip('"!?.,[]{}<>;:@#$%^&*()|/-+'):
                if c in "eyuioa":
                    vowels += 1
                else:
                    consonants += 1
            print(f"Строка {elem} содержит {vowels} гласных и {consonants} согласных")


list_ = [15, 48, 'hello', 6, 19, 'world']

numbers(list_)
chars(list_)
