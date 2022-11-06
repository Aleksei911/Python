from DZ.KOHNUK_104_lesson18.Tomato import Tomato


class TomatoBush(Tomato):

    def __init__(self, num: int):
        self.tomatoes = [Tomato.__init__(self, i) for i in range(num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            Tomato(tomato).grow()

    def all_are_ripe(self) -> bool:
        return all(map(lambda x: Tomato(x).is_ripe(), self.tomatoes))

    def give_away_all(self):
        self.tomatoes.clear()
