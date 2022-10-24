# задание 1

# creating a new file
with open('task_1.txt', 'w', encoding='utf-8'):
    pass


# задание 2

# write numbers and letters to a file on different lines

def division(string: str) -> tuple:
    numbers = ' '.join(filter(lambda x: x.isdigit(), string.split()))
    strings = ' '.join(filter(lambda x: x.isalpha(), string.split()))
    return numbers, strings


try:
    user_input = division(input('Введите слова и числа через пробел: '))
except Exception:
    print('Проверьте корректность вводимых данных!')
else:
    with open('task_2.txt', 'w', encoding='utf-8') as file:
        print(user_input[0], file=file)
        print(user_input[1], file=file)


# задание 3

with open('task_3.txt') as f:
    file = f.read().replace('\n', ' ').split()
    total = map(lambda x: int(x) if x.isdigit() else x, file)
    print(*sorted(total, key=lambda x: (isinstance(x, str),
                                        len(x) if isinstance(x, str) else x,
                                        x.lower() if isinstance(x, str) else x)))


# additional task 1

