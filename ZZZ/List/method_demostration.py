example_list = [1, 'строка', [1, 2, 3], 1]  # список
"""
В первой строке кода объявлена переменная example_list, которая ссылается на список,
состоящий из значений: 1, 'строка', [1, 2, 3], 1
Каждый отдельный объект в представленном списке относится к определенному типу данных
   1      - integer (или число)
'строка'  - string (или строка)
[1, 2, 3] - list (или список), находящийся внутри списка example_list
   1      - integer (или число)
   
Сам список example_list представляет собой отдельный объект list, к которому 
мы можем использовать методы, которые относятся к списку 


example_list.append(x) - добавляет объект x в список
example_list.extend(x) - расширяет список элементами объекта из объекта х (например списка)
example_list.insert(i, x) - вставляет значение x в индекс i
example_list.clear() - очищает список от всех объектов, находящихся внутри него
example_list.index(x) - 
"""




# функция для переворота списка
example_list.reverse()
# было: >>> [1, 'строка', [1, 2, 3], True]
# стало: >>> [True, [1, 2, 3], 'строка', 1]

# функция для подсчета повторений значения
print(example_list.count(1))
