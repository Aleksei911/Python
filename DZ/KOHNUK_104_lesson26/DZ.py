import sqlite3

'''Создать 2 таблицы в Базе Данных
Одна будет хранить текстовые данные(1 колонка)
Другая числовые(1 колонка)
Есть список, состоящий из чисел и слов.
Если элемент списка слово, записать его в
соответствующую таблицу, затем посчитать длину слова и
записать её в числовую таблицу
Если элемент списка число: проверить, если число чётное
записать его в таблицу чисел, если нечётное, то записать во
вторую таблицу слово: «нечётное»
Если число записей во второй таблице больше 5, то удалить
1 запись в первой таблице. Если меньше, то обновить 1
запись в первой таблице на «hello»'''

dz_base = sqlite3.connect('dz_base.db')
cursor = dz_base.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS 
                        dz1(
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            col TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS 
                        dz2(
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            col INTEGER)''')

data = ['fdsf', 'dsas', 56, 'tw', 18, 31, 'rtw', 4]

for elem in data:
    if isinstance(elem, str):
        cursor.execute('''INSERT INTO dz1(col) VALUES (?)''', (elem,))
        cursor.execute('''INSERT INTO dz2(col) VALUES (?)''', (len(elem),))
    else:
        if elem % 2 == 0:
            cursor.execute('''INSERT INTO dz2(col) VALUES (?)''', (elem,))
        else:
            cursor.execute('''INSERT INTO dz1(col) VALUES ('нечётное')''')

cursor.execute('''SELECT COUNT(*) FROM dz2''')
if cursor.fetchall()[0][0] > 5:
    cursor.execute('''DELETE FROM dz1 WHERE id=1''')
else:
    cursor.execute('''UPDATE dz1 SET col='hello' WHERE id=1''')
