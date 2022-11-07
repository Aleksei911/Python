class Tomato:
    states = {1: 'росток',
              2: 'цветение',
              3: 'появление плодов',
              4: 'созревание плодов',
              5: 'готово'}

    def __init__(self, index: int):
        self._index = index
        self._state = 1

    def grow(self):
        if self._state != 5:
            self._state += 1
            print(Tomato.states[self._state])

    def is_ripe(self) -> bool:
        return self._state == 5
