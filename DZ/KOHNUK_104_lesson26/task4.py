import sqlite3
from task4_class import DB

'''Создайте метод класса для работы с БД
В БД
Если передан 1 аргумент, вставить в таблицу запись с
числом 3
Если переданы 2 аргумента: проверить или второй
аргумент является числом. Если условие верно, то
удалить первую запись с БД
Если переданы 2 аргумента, их значения неизвестны, а 3
является числом, то обновить на число 77 запись 3.'''

base4 = sqlite3.connect('task4.db')
cursor4 = base4.cursor()

cursor4.execute('''CREATE TABLE IF NOT EXISTS task4(id INTEGER PRIMARY KEY AUTOINCREMENT, num INTEGER)''')

db = DB(cursor4)
db.base_maker('task4', '1')

cursor4.execute('''SELECT * FROM task4''')
print(cursor4.fetchall())
