import BlackJackfunction

import random
import time
PLAYER = 0
DEALER = 1

class player:
    def __init__(self) -> None:
        self.cards = []


    def hit(self):
        self.cards.append(BlackJackfunction.genrateCard(self.cards))

    def sum(self):
        return sum(self.cards)