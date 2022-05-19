from hand import Hand

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def get_str_hand(self):
        print(f"The dealer has: {self.hand.__str__()}")

    def initial_dealt(self, cards):
        self.hand.add_to_hand(cards)

        print(f"The dealer is dealt: {cards[0].__str__()}, Unknown")

    def hit(self, cards):
        self.hand.add_to_hand(cards)

        print(f"The dealer hits and is dealt: {cards[0].__str__()}")
