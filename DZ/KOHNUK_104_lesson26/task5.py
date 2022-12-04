import sqlite3

'''Создать таблицу в Базе Данных с тремя колонками(id, 2 -
text, 3 - text).
Заполнить её с помощью INSERT данными (3 записи).
Удалить с помощью DELETE 2 запись. Обновить значения
3-ей записи на: hello world с помощью UPDATE
*Записать данные с таблицы в файл в три колонки.
Первая – id, вторая и третья с данными.'''

base5 = sqlite3.connect('task5.db')
cursor5 = base5.cursor()

cursor5.execute('''CREATE TABLE IF NOT EXISTS task5(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    two TEXT,
                    three TEXT)''')

cursor5.execute('''INSERT INTO task5(two, three)
                    VALUES ('one', 'two'), ('three', 'four'), ('five', 'six')''')

cursor5.execute('''DELETE FROM task5 WHERE id=2''')

cursor5.execute('''UPDATE task5 SET two='hello', three='world' WHERE id=3''')

cursor5.execute('''SELECT * FROM task5''')

with open('task5.txt', 'w') as file:
    for row in cursor5.fetchall():
        print(f'{row[0]}    {row[1]}    {row[2]}', file=file)
