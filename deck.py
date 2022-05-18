import random
from card import Card


class Deck:
    def __init__(self):
        self.cards_in_deck = self.create_deck()
        self.shuffle()

    def create_deck(self):
        deck = []

        for suit in range(4):
            for value in range(1, 14):
                deck.append(Card(suit, value))
        
        return deck

    def shuffle(self):
        random.shuffle(self.cards_in_deck)

    def deal(self, num_cards):
        cards_dealt = []

        for _ in range(num_cards):
            cards_dealt.append(self.cards_in_deck.pop())

        return cards_dealt