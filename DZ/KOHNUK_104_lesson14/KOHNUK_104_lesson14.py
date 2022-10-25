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

# sort the data from the file so that the numbers are in ascending order,
# and the lines are in increasing length

with open('task_3.txt') as f:
    file = f.read().replace('\n', ' ').split()
    total = map(lambda x: int(x) if x.isdigit() else x, file)
    print(*sorted(total, key=lambda x: (isinstance(x, str),
                                        len(x) if isinstance(x, str) else x,
                                        x.lower() if isinstance(x, str) else x)))


# additional task 1

# create a square matrix and check if it is a magic square

def create_matrix(num: int) -> list:
    matrix = []
    for i in range(num):
        temp = [int(j) for j in input(f'Введите {num} чисел через пробел: ').split()]
        matrix.append(temp)
    return matrix


def check_sum_lines(any_list: list) -> bool:
    first = sum(any_list[0])
    total = map(lambda x: sum(x) == first, any_list)
    return all(total)


def check_sum_columns(any_list: list) -> bool:
    temp = []
    for i in range(size):
        temp.append(sum([line[i] for line in any_list]))
    first = temp[0]
    total = [num == first for num in temp]
    return all(total)


def check_sum_diagonals(any_list: list) -> bool:
    main_diagonal = sum([any_list[i][i] for i in range(size)])
    secondary_diagonal = sum([any_list[i][size - i - 1] for i in range(size)])
    return main_diagonal == secondary_diagonal


try:
    size = int(input('Введите размерность квадратной матрицы: '))
except ValueError:
    print('Нужно ввести число!')
else:
    try:
        matrix = create_matrix(size)
    except Exception:
        print('Некорректные данные для заполнения матрицы!')
    else:
        result = all((check_sum_lines(matrix),
                      check_sum_columns(matrix),
                      check_sum_diagonals(matrix)))
        if result:
            print('Ваша матрица является магическим квадратом!')
        else:
            print('Ваша матрица не является магическим кварратом!')


# DZ

def sort_func(array: list):
    total = map(lambda x: int(x) if x.isdigit() else x, array)
    return sorted(total, key=lambda x: (isinstance(x, int),
                                        len(x) if isinstance(x, str) else x,
                                        x.lower() if isinstance(x, str) else x))


user_input = input('Введите слова и числа через пробел: ').split()
print(sort_func(user_input))
