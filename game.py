from deck import Deck
import math

class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def dealer_turn(self):
        self.dealer.get_str_hand()
        
        while (self.dealer.hand.get_value() <= 16):
            self.dealer.hit(self.deck.deal(1))
            self.dealer.get_str_hand()

            if (self.dealer.hand.get_value() > 16 and self.dealer.hand.get_value() <= 21):
                print("The dealer stays.")

        if (self.dealer.hand.get_value() > 21 or self.dealer.hand.get_value() < self.player.hand.get_value()):
            if (len(self.player.hand.cards) == 2 and self.player.hand.get_value() == 21):
                print(f"Blackjack! You win ${(self.bet * 1.5):.2f} :)")
                self.player.update_balance(self.bet * 1.5)
                print()
            else:
                print(f"The dealer busts, you win ${self.bet:.2f} :)")
                self.player.update_balance(self.bet)
                print()
        elif (self.dealer.hand.get_value() == self.player.hand.get_value()):
            print("You tie. Your bet has been returned.")
            print()
        elif (self.dealer.hand.get_value() > self.player.hand.get_value()):
            print(f"The dealer wins, you lose ${self.bet:.2f} :(")
            self.player.update_balance(-self.bet)
            print()

    def start_game(self):
        answer = input(f"You are starting with ${self.player.balance}. Would you like to play a hand? ")

        if answer == "yes":
            while True:
                self.bet = float(input("Place your bet: "))
                if (self.bet > Game.MINIMUM_BET):
                    if (self.bet <= self.player.balance): 
                        break
                    else:
                        print("You do not have sufficient funds.")
                else:
                    print(f"The minimum bet is ${Game.MINIMUM_BET}")
            
            self.player.hit(self.deck.deal(2))
            self.dealer.initial_dealt(self.deck.deal(2))
            
            if (self.player.hand.get_value() == 21):
                self.dealer_turn()
            else:
                while True:
                    hit_or_stay = input("Would you like to hit or stay? ")

                    if hit_or_stay == "hit":
                        self.player.hit(self.deck.deal(1))

                        if (self.player.hand.get_value() > 21):
                            print(f"Your hand value is over 21 and you lose ${self.bet:.2f} :(")
                            self.player.update_balance(-self.bet)
                            break
                        else:
                            print(f"You now have: {self.player.hand}")
                    elif hit_or_stay == "stay":
                        self.dealer_turn()
                        break
                    else:
                        print("That is not a valid option.")

            self.player.hand.reset_hand()
            self.dealer.hand.reset_hand()
            self.deck = Deck()

            if (self.player.balance > 0):
                self.start_game()
            else:
                print("You've ran out of money. Please restart this program to try again. Goodbye.")