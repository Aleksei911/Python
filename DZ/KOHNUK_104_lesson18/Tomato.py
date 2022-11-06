class Tomato:
    states = {1: 'росток',
              2: 'цветение',
              3: 'появление плодов',
              4: 'созревание плодов',
              5: 'готово'}

    def __init__(self, index: int):
        self._index = index
        self.key = 1
        self._state = Tomato.states[self.key]

    def grow(self):
        if self.key != 5:
            self.key += 1
            self._state = Tomato.states[self.key]
            print(self._state)

    def is_ripe(self) -> bool:
        return self._state == 'готово'
