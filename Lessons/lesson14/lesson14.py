import os

f = open('example.txt', 'r')

try:
    print(*f)
finally:
    f.close()

#######################################

with open('example.txt') as f:
    print(*f)

#######################################

f = open('example.txt', 'r')  # чтение 7 символов их example.txt

print(f.read(7))

f.close()

#######################################


x = open('test.txt', 'r')

print(x.readline())
print(x.readline())

x.close()

#######################################

x = open('test.txt', 'r')

print(x.readlines())

x.close()

#######################################

# os.rename('test_14/test.txt', 'test_14/new_test.txt')

#######################################

print('Текущая деректория: ', os.getcwd())  # вывести текущую директорию

os.mkdir('test_14/folder')  # согдать пустой каталог с этим названием

#######################################

# задание 1

with open('example.txt') as file:
    f = file.read().replace('_', ' ')
    total = 0
    for elem in f.split():
        if elem.isdigit():
            total += int(elem)
print(total)

# задание 2

with open('task_2.txt') as file:
    f = file.read().split('\n')
    total = map(lambda x: int(x) if x.isdigit() else x, f)
print(sorted(total, key=lambda x: (isinstance(x, str), x)))

# задание 3

with open('task_3.txt', 'w', encoding='utf-8') as file:
    s = input('Введите строку: ')
    while s != '':
        print(s, file=file)
        s = input('Введите строку: ')

# задание 4

with open('task_4.txt') as file:
    total = file.readlines()
    print(f'В файле содержится {len(total)} строк(и)')
    for lane in total:
        print(f'В {total.index(lane) + 1} строке {len(lane)} символов!')
