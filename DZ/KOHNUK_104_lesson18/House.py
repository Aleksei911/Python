class House:
    def __init__(self, area:int, price: int):
        self._area = area
        self._price = price

    def final_price(self, value: int) -> float:
        return round(self._price * (1 - value / 100), 2)


