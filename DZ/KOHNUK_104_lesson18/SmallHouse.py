from DZ.KOHNUK_104_lesson18.House import House


class SmallHouse (House):

    DEFAULT_AREA = 40

    def __init__(self, price):
        House.__init__(self, price=price, area=SmallHouse.DEFAULT_AREA)


