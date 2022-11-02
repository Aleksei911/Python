class Human:
    default_name = 'Alexey'
    default_age = 29

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 100000
        self.__house = 'Minsk'

    def info(self):
        print(f'Name: {self.name}, age: {self.age}, house: {self.__house}, money: {self.__money}')

    @staticmethod
    def default_info():
        print(f'default_name: {Human.default_name}, default_age: {Human.default_age}')

    def earn_money(self, value):
        self.__money += value


Human().default_info()
test = Human('Sasha', 56)
test.info()
test.earn_money(500)
test.info()
