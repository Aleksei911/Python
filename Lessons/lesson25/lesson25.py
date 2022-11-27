import os


# class Something:
#
#     # переопределяем метод __new__, в котором обязательно делаем ссылку на текущий класс, также указываем
#     # на прием неограниченного количества позиционных и ключевых аргументов
#
#     def __new__(cls, *args, **kwargs):
#         # выведем сообщение о том, что наш метод __new__ сработал
#         print(f'Сработал __new__, переданы аргументы {args, kwargs}')
#
#         # теперь мы, к примеру, решили на этапе создания объекта добавить новый атрибут, для этого мы
#         # переопределяем __new__ родителя (object)
#         instance = super().__new__(cls)
#
#         # добавляем к экземпляру новый атрибут
#         instance.new_attribute = 'добавлено'
#
#         # в результате работы функции мы должны вернуть объект
#         # в нашем случае instance
#         return instance
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# example = Something('Igor', 24)
# print(example.__dir__())


class FileObject:
    def __init__(self, filename):
        self.filename = open(filename, 'r')

    def __del__(self):
        self.filename.close()
        print('Файл закрыт')
        if os.path.isfile('data.txt'):
            os.remove('data.txt')
            print('Удалено')
        else:
            print('Файл не найден')

    def read_file(self):
        print('Открываем файл и выводим на печпть')
        print(*self.filename.readlines())
        print('Печать завершена')


ob = FileObject('data.txt')
ob.read_file()
del ob
