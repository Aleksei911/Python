class Word(str):
    # класс для сравнения слов

    def __new__(cls, word):
        # мы должны использовать __new__, т.к. тип str неизменяемый
        # и мы должны инициализировать его раньше (при создании)
        if ' ' in word:
            # если введенное слово содержит пробел - обрезаем символы до него
            word = word[:word.index(' ')] # теперь Word это все символы до первого пробела
            # с учетом того что это строка, вызываем __new__ у класса str
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)