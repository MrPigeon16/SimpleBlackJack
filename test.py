import random

def genrateCard(deck):
    sum_deck = sum(deck)
    random_number = random.randint(1,2)
    if sum_deck < 11 and random_number == 1:
        return 11
    else:
        return random_number

x = [1]

print(genrateCard(x))