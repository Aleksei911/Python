import string

# DZ

"""
Два метода в классе, один принимает в семя либо строку, либо число.
Если я передаю строку, то смотрим:
если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные
иначе выводить все согласные
Если число - вывести произведение суммы четных цифр на длину числа
Длину строки и числа искать во втором методе
"""


class Homework:

    def one(self, something):
        # если число - делаем по ТЗ
        if isinstance(something, int):
            evens = [int(x) for x in str(something) if int(x) % 2 == 0]
            print(sum(evens) * self.length(something))
        elif isinstance(something, str):
            # если строка состоящая из цифр - преобразуем к числу и делаем по ТЗ
            if something.isdigit():
                self.one(int(something))
            # иначе - делаем по ТЗ как обычную строку
            else:
                vowels = ''.join([x for x in something.lower() if x in 'eyuioa'])
                consonants = ''.join(
                    [x for x in something.lower() if x in string.ascii_lowercase and x not in 'eyuioa'])
                if self.length(vowels) * self.length(consonants) == 0:
                    print('The string does not contain letters')
                elif self.length(vowels) * self.length(consonants) <= self.length(something):
                    print(vowels)
                else:
                    print(consonants)

    def length(self, value):
        if isinstance(value, int):
            return len(str(value))
        else:
            return len(value)


if __name__ == '__main__':
    obj_one = Homework()
    obj_one.one('@#$$%^&&')
