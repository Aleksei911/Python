# Задание № 1

inp_str, inp_symb, clear_str = input('Введите строку:'), \
                               input('Введите символ: '), \
                               ''
for symb in inp_str:
    # проходим по каждому символу строки
    if symb != inp_symb:
        # если символ != введенному символу
        clear_str += symb
        # записываем его в новую строку
print(clear_str)

# Задание № 2

start, end, step = int(input('Введите начало: ')), \
                   int(input('Введите конец: ')), \
                   int(input('Введите шаг: '))
for elem in range(start, end, step):
    print(elem)

# Задание № 3

for elem in range(54, 9184):
    if elem % 5 == 0:
        print(elem)
    else:
        pass
