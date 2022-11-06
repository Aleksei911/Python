from DZ.KOHNUK_104_lesson18.Alphabet import Alphabet
import string


class EngAlphabet(Alphabet):
    __letters_num = len(string.ascii_uppercase)

    def __init__(self):
        Alphabet.__init__(self, lang='En', letters=string.ascii_uppercase)

    def is_en_letter(self, char: str) -> bool:
        return char.upper() in self.letters

    def letters_num(self) -> int:
        return EngAlphabet.__letters_num

    @staticmethod
    def example() -> str:
        return 'This string is an example'


al = EngAlphabet()
al.print()
print(al.letters_num())
print(al.is_en_letter('F'))
print(al.is_en_letter('Щ'))
print(al.example())