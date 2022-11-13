import asyncio
import time


async def fun1(x):
    print('Запуск fun1...')
    print(x ** 2)
    print('fun1 засыпает...')
    await asyncio.sleep(3)
    print('...fun1 очнулась и завершена')


async def fun2(x):
    print('Запуск fun2...')
    print(x ** 0.5)
    print('fun2 засыпает...')
    await asyncio.sleep(3)
    print('...fun2 очнулась и завершена')


print(time.strftime('%X'), ': программа запущена')

loop = asyncio.get_event_loop()
task1 = loop.create_task(fun1(4))
task2 = loop.create_task(fun2(4))
loop.run_until_complete(asyncio.wait([task1, task2]))

print(time.strftime('%X'), ': программа завершена')
