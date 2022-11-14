import random


class CardDeck:
    DECK = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SHIRT = ['clubs', 'diamonds', 'hearts', 'spades']

    def __init__(self):
        self.card_deck = [i + ' ' + j for j in CardDeck.SHIRT for i in CardDeck.DECK]

    def __iter__(self):
        random.shuffle(self.card_deck)
        self.value = -1
        return self

    def __next__(self):
        self.value += 1
        if self.value <= len(self.card_deck) -1:
            return self.card_deck[self.value]
        else:
            raise StopIteration