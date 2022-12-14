elems = [1, 2, 3]
"""
Вернемся к нашему списку и попробуем пройтись по 
всем объектам внутри нашего списка. 
"""

for _ in elems:
    print(_)

"""
Подобный пример мы уже неоднократно использовали. 
Мы подавали в наш цикл for итерабельный объект. 
Ранее мы не углублялись в процесс работы подобной конструкции.
Однако теперь, необходимо запомнить следующее.
Когда мы перебираем элементы списка (или другого итерабельного объекта)
к нему применяется функция iter(), чтобы создать итератор, а затем
у этого объекта вызывается метод __next__ до тех пор, пока не 
возникнет исключение StopIteration. 
Итераторы в первую очередь полезны тем, что они отдают элементы
по одному. Например, при работе с файлом это полезно тем, что
в памяти будет находиться не весь файл, а только одна строка файла. 
"""