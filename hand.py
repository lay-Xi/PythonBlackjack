class Hand:
    def __init__(self):
        self.cards = []

    def get_value(self):
        value = 0
        ace_count = 0
        
        for card in self.cards:
            if card.value in ["T", "J", "Q", "K"]:
                value += 10
            elif card.value == "A":
                value += 11
                ace_count += 1
            else:
                value += int(card.value)
        
        while value > 21 and ace_count > 0:
            value -= 10
            ace_count -= 1

        return value
        
    def add_to_hand(self, card):
        self.cards.append(card)

    def __str__(self):
        hand = ""
        for card in self.cards:
            hand += f"{card.__str__()}, "

        return hand[:-2]