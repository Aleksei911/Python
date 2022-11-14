from CardDeck import CardDeck

'''
Реализуйте итератор колоды карт (52 штуки) CardDeck.
Каждая карта представлена в виде строки типа «2 Пик».
При вызове функции next() будет представлена
следующая карта. По окончании перебора всех
элементов возникнет ошибка StopIteration.
'''

if __name__ == '__main__':
    new_card_deck = CardDeck()
    iteration_card_deck = iter(new_card_deck)
    for _ in range(53):
        print(iteration_card_deck.__next__())