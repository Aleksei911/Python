from DZ.KOHNUK_104_lesson18.Tomato import Tomato


class TomatoBush(Tomato):

    def __init__(self, index: int, num: int):
        super().__init__(index)
        self.tomatoes = [Tomato(i) for i in range(num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        if not self.tomatoes:
            print('Посадить новый урожай')
        else:
            return all(map(lambda x: x.is_ripe(), self.tomatoes))

    def give_away_all(self):
        self.tomatoes.clear()
