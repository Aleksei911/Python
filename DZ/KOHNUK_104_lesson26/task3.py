import sqlite3
from random import randint

'''Создайте новую Базу данных
Поля: id, 2 целочисленных поля
Целочисленные поля заполняются рандомно от 0 до 9
Выберите случайную запись из БД
Если каждое число данной записи чётное, то удалите эту
запись, если нечётное, то обновите данные в ней на(2,2)'''

base3 = sqlite3.connect('task3.db')
cursor3 = base3.cursor()

cursor3.execute('''
    CREATE TABLE IF NOT EXISTS
    task3(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        num1 INT,
        num2 INT
    )
    ''')

for _ in range(5):
    cursor3.execute('''
        INSERT INTO task3(num1, num2)
        VALUES (?, ?)''', (randint(0, 10), randint(0, 10)))

cursor3.execute('''SELECT num1, num2 FROM task3 WHERE id=?''', (randint(1, 6),))
random_value = cursor3.fetchall()[0]

print(f'Случайные значения равны: {random_value}')

if random_value[0] % 2 == 0 and random_value[1] % 2 == 0:
    cursor3.execute('''DELETE FROM task3 WHERE num1 = ? AND num2 = ?''', (random_value[0], random_value[1]))
    print('Запись была успешно удалена')
    cursor3.execute('''SELECT * FROM task3''')
    print(cursor3.fetchall())
else:
    cursor3.execute('''UPDATE task3
                       SET num1 = 2,
                           num2 = 2
                       WHERE num1 = ? AND num2 = ?''', (random_value[0], random_value[1]))
    print('Запись была успешно заменена')
    cursor3.execute('''SELECT * FROM task3''')
    print(cursor3.fetchall())
