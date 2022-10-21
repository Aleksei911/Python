# DZ

def division(any_string: str) -> float:
    while True:
        temp = any_string.split()
        if len(temp) == 2:
            try:
                return int(temp[0]) / int(temp[1])
            except ZeroDivisionError:
                print('На ноль делить нельзя!')
                any_string = input('Введите новые данные: ')
            except ValueError:
                print('Введённые данные не авляются числами!')
                any_string = input('Введите новые данные: ')
        else:
            print('Нужно ввести именно 2 числа через пробел!')
            any_string = input('Введите новые данные: ')


print(division(input('Введите 2 числа через пробел: ')))
