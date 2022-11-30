import sqlite3

# Создаем Базу данных
conn = sqlite3.connect('name.db')
# Создаем объект cursor, который позволяет нам взаимодействовать с базой данных
cursor = conn.cursor()
# Создадим таблицу с двумя текстовыми колонками
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS
    tab_1(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col_1 TEXT,
    col_2 TEXT)'''
)

cursor.execute('''
    INSERT INTO tab_1(col_1, col_2)
    VALUES('helo', 'world')
''')
# ОБЯЗАЧЕЛЬНО СОХРАНЯЕМ ИЗМЕНЕНИЯ
conn.commit()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS
    tab_2(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col_1 TEXT,
    col_2 TEXT)'''
)

var1 = 'red'
var2 = 'black'

command = '''
    INSERT INTO tab_2(col_1, col_2)
    VALUES(?,?)
'''

cursor.execute('''
    INSERT INTO tab_2(col_1, col_2)
    VALUES(?,?)''', (var1, var2))

data_list = [('yellow', 'white') for x in range(10)]

for tuple_ in data_list:
    cursor.execute(command, tuple_)

conn.commit()

cursor.execute('''SELECT * FROM tab_2''')
print(cursor.fetchall())

#############################################

command = '''
    INSERT INTO tab_1(col_1, col_2)
    VALUES (?,?)'''

for _ in range(10):
    cursor.execute(command, (input('введите текст: '), input('введите текст: ')))

conn.commit()

########################################

cursor.execute('''SELECT col_1 FROM tab_2 WHERE col_1 LIKE '%yell%' ''')
print(cursor.fetchall())

########################################

# задание 1

new_conn = sqlite3.connect('data.db')
my_cursor = new_conn.cursor()

new_conn.execute('''
    CREATE TABLE IF NOT EXISTS
    my_tab(
    col1 TEXT,
    col2 TEXT,
    col3 INT)
''')

for _ in range(5):
    new_conn.execute('''
        INSERT INTO my_tab(col1, col2, col3)
        VALUES (?, ?, ?)''', ('one', 'two', int(input('Введите число: '))))

new_conn.commit()

# for i in new_conn.execute('''SELECT * FROM my_tab'''):
#     print(i)
print(*new_conn.execute('''SELECT * FROM my_tab'''), sep='\n')
