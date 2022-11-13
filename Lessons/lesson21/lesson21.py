import time


def fun1(x):
    print('Запуск fun1...')
    print(f'x ** 2 = {x ** 2}')
    print('fun1 засыпает...')
    time.sleep(3)
    print('...fun1 очнулась и завершена')


def fun2(x):
    print('Запуск fun2...')
    print(f'x ** 0.5 = {x ** 0.5}')
    print('fun2 засыпает...')
    time.sleep(3)
    print('...fun2 очнулась и завершена')


def main():
    fun1(4)
    fun2(4)


print(time.strftime('%X'), ': программа запущена')

main()

print(time.strftime('%X'), ': программа завершена')
