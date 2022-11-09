import logging


def debug(func):
    # получение пользовательского логгера и установка уровня логирования
    loger = logging.getLogger(__name__)
    loger.setLevel(logging.INFO)

    # настройка обработчика и форматировщика в соответствии с нашими нуждами
    my_handler = logging.FileHandler(f'{__name__}.log', mode='w', encoding='UTF-8')
    my_formatter = logging.Formatter('%(name)s %(asctime)s %(levelname)s %(message)s')

    # добавление форматировщика к обработчику
    my_handler.setFormatter(my_formatter)

    # добавление обработчика к логгеру
    loger.addHandler(my_handler)

    loger.info(f'Starting  the logger for module {__name__}...')

    def wrapper(*args, **kwargs):
        loger.info(f'Calling the {func.__name__} function by passing arguments {*args, *kwargs} to it')
        try:
            result = func(*args, **kwargs)
            loger.info(f'the result of the function is {result}')
            return result
        except ZeroDivisionError:
            loger.exception("ZeroDivisionError")

    return wrapper


@debug
def delitel(a, b):
    return a / b


if __name__ == '__main__':
    delitel(10, 2)
    delitel(4, 0)
