from DZ.KOHNUK_104_lesson18.House import House
from DZ.KOHNUK_104_lesson18.SmallHouse import SmallHouse


class Human:
    default_name = 'Alexey'
    default_age = 29

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 10000
        self.__house = 'Minsk'

    def info(self) -> None:
        print(f'Name: {self.name}, age: {self.age}, house: {self.__house}, money: {self.__money}')

    @staticmethod
    def default_info() -> None:
        print(f'default_name: {Human.default_name}, default_age: {Human.default_age}')

    def earn_money(self, value: int) -> None:
        self.__money += value

    def __make_deal(self, house_obj: House, value: float) -> None:
        self.__money -= value
        self.__house = house_obj

    def buy_house(self, house_obj: House, discount: int) -> None:
        total_price = house_obj.final_price(discount)
        print(total_price)
        if self.__money >= total_price:
            self.__make_deal(house_obj, total_price)
        else:
            print('Недостаточно денег!')


# вызываем справочный метод
Human().default_info()
# создаем объект класса
test = Human('Sasha', 56)
# выводим справочную информацию
test.info()
# поправляем финансовое положение
test.earn_money(500)
# выводим справочную информацию
test.info()

# создаем объект класса
s = SmallHouse(110000)
# пытаемся купить дом
test.buy_house(s, 10)
# поправляем финансовое положение
test.earn_money(100000)
# пытаемся купить дом снова
test.buy_house(s, 10)
# выводим справочную информацию
test.info()
