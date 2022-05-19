from deck import Deck
import math

class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def start_game(self):
        answer = input(f"You are starting with {self.player.balance}. Would you like to play a hand? ")

        if answer == "yes":
            while True:
                self.bet = float(input("Place your bet: "))
                if (self.bet > Game.MINIMUM_BET):
                    if (self.bet < self.player.balance): 
                        break
                    else:
                        print("You do not have sufficient funds.")
                else:
                    print(f"The minimum bet is ${Game.MINIMUM_BET}")
            
            self.player.hit(self.deck.deal(2))
            self.dealer.hit(self.deck.deal(2))

            while True:
                hit_or_stay = input("Would you like to hit or stay? ")

                if hit_or_stay == "hit":
                    self.player.hit(self.deck.deal(1))
                    if (self.player.hand.get_value() > 21):
                        print(f"Your hand value is over 21 and you lose ${self.bet:.2f} :(")
                        self.player.update_balance(-self.bet)
                        break
                    else:
                        print(self.player.hand)
                elif hit_or_stay == "stay":
                    break
                else:
                    print("That is not a valid option.")
