try:
    k = 1 / 0
except ZeroDivisionError:
    k = 0

print(k)

#############################################


my_dict = {'a': 1, 'b': 2, 'c': 3}

try:
    value = my_dict['d']
except KeyError:
    print('Ключа не существует!')

#############################################


my_list = [1, 2, 3, 4, 5]

try:
    my_list[6]
except IndexError:
    print('Этого индекса нет в списке!')

#############################################


my_dict = {'a': 1, 'b': 2, 'c': 3}

try:
    value = my_dict['d']
except IndexError:
    print('Такого индекса не существует!')
except KeyError:
    print('Этого ключа нет в словаре!')
except:
    print('произошла другая ошибка!')

#############################################


my_dict = {'a': 1, 'b': 2, 'c': 3}

try:
    value = my_dict['d']
except KeyError:
    print('Произошла ошибка KeyError!')
finally:
    print('Оператор finally выполнен!')

#############################################

my_dict = {'a': 1, 'b': 2, 'c': 3}

try:
    value = my_dict['d']
except KeyError:
    print('Произошла ошибка KeyError!')
else:
    print('Ошибок не произошло!')
finally:
    print('Оператор finally выполнен!')


# задание 3

def summa(num1, num2):
    try:
        return num1 + num2
    except Exception:
        print('Проверьте вводимые данные!')


def difference(num1, num2):
    try:
        return num1 - num2
    except Exception:
        print('Проверьте вводимые данные!')


def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('На ноль дельть нельзя!')
    except Exception:
        print('Проверьте вводимые данные!')


def multi(num1, num2):
    try:
        return num1 * num2
    except Exception:
        print('Проверьте вводимые данные!')


def calc(string, num1, num2):
    my_dict = {'+': summa(num1, num2),
               '-': difference(num1, num2),
               '/': division(num1, num2),
               '*': multi(num1, num2)}
    return my_dict[string]


num1 = int(input('введите 1 число: '))
num2 = int(input('введите 2 число: '))
sign = input('введите действие: ')

print(calc(sign, num1, num2))


###############################################


def calc2(total: tuple):
    my_dict = {'+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '/': lambda x, y: x / y,
               '*': lambda x, y: x * y}
    try:
        return my_dict[total[0]](total[1], total[2])
    except ZeroDivisionError:
        return 'На ноль дельть нельзя!'
    except KeyError:
        return 'Такое действие не предусмотрено'
    except Exception:
        return 'Проверьте вводимые данные!'


def req():
    num1 = int(input('введите 1 число: '))
    num2 = int(input('введите 2 число: '))
    sign = input('введите действие: ')
    return sign, num1, num2


print(calc2(req()))
