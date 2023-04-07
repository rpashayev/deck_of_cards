from . import card
from random import randint

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def draw_card(self):
        if len(self.cards) > 0:
            self.current_card = self.cards[randint(0, len(self.cards)-1)]
            self.value = self.current_card.point_val
            self.cards.remove(self.current_card)
        return self 

    def show_card(self):
        self.current_card.card_info()
        return self
