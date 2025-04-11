import random

suits = ['Diamonds', 'Spades', 'Hearts', 'Clubs']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = []

for suit in suits:
    for rank in ranks:
        card = (rank, suit)
        deck.append(card)

random.shuffle(deck)

for card in deck:
    print(f"{card[0]} of {card[1]}")

