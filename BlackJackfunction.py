import time
import random



def welcome_msg():
    print("WELCOME TO BLACKJACK!, The new way to make money WITHOUT EVER LOSING!")
    print("JK, There is no betting system (YET) right now you will just play the game")

    


def genrateCard(deck):
    sum_deck = sum(deck)
    random_number = random.randint(1,10)
    if sum_deck < 11 and random_number == 1:
        return 11
    else:
        return random_number

    














