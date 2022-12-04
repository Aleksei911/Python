import sqlite3
from random import randint

'''Создайте новую Базу данных.
Поля: id, 2 целочисленных поля
Целочисленные поля заполняются рандомно от 0 до 9
Посчитайте среднее арифметическое всех элементов без
учёта id
Если среднее арифметическое больше количества записей в
БД, то удалите четвёртую запись БД'''

base2 = sqlite3.connect('task2.db')
cursor2 = base2.cursor()

cursor2.execute('''
    CREATE TABLE IF NOT EXISTS
    task2(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        num1 INT,
        num2 INT
    )
    ''')

for _ in range(50):
    cursor2.execute('''
        INSERT INTO task2(num1, num2)
        VALUES (?, ?)''', (randint(0, 100), randint(0, 100)))

# print(*cursor.execute('''SELECT * FROM task2'''))

cursor2.execute('''SELECT AVG(num1 + num2) / 2 FROM task2''')
avg = cursor2.fetchall()[0][0]
print(f'Среднее арифметическое всех элементов равно: {avg}')

cursor2.execute('''SELECT COUNT(*) FROM task2''')
count = cursor2.fetchall()[0][0]
print(f'Количество записей в БД: {count}')

if avg > count:
    cursor2.execute('''DELETE FROM task2 WHERE id=4''')
    print('4 запись БД удалена')
