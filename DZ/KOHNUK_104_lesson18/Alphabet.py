class Alphabet:
    def __init__(self, lang: str, letters: str):
        self.lang = lang
        self.letters = list(letters)

    def print(self) -> None:
        print(*self.letters)

    def letters_num(self) -> int:
        return len(self.letters)