from DZ.KOHNUK_104_lesson18.TomatoBush import TomatoBush


class Gardener:
    def __init__(self, name: str, plant: TomatoBush):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self) -> None:
        if self._plant.all_are_ripe():
            print('Собираем урожай')
            self._plant.give_away_all()
        else:
            print('Урожай ещё не созрел!')

    @staticmethod
    def knowledge_base() -> None:
        print('something')


if __name__ == '__main__':
    Gardener.knowledge_base()
    tom = TomatoBush(1, 5)
    gar = Gardener('Vasya', tom)
    gar.work()
    gar.harvest()
    gar.work()
    gar.harvest()
    gar.work()
    gar.harvest()
    gar.work()
    gar.harvest()
