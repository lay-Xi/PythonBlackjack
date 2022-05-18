from hand import Hand

class Player:
    def __init__(self, balance):
        self.balance = balance
        self.hand = Hand()

    def get_str_hand(self):
        print(f"You now have: {self.hand.__str__()}")

    def hit(self, cards):
        self.hand.add_to_hand(cards)

        cards_dealt = ""
        for card in cards:
            cards_dealt += f"{card}, "

        print(f"You are dealt: {cards_dealt[:-2]}")

    def update_balance(self, amount):
        self.balance += amount
