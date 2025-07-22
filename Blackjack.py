import random

suits = ['Diamonds', 'Spades', 'Hearts', 'Clubs']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = [(rank, suit) for suit in suits for rank in ranks]
random.shuffle(deck)

# Deal cards
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

# Format hands
def format_hand(hand):
    return ', '.join(f"{card[0]} of {card[1]}" for card in hand)


def cal_hand_val(hand):
    value=0
    aces=0

    for card in hand:
        rank = card[0]

        if rank in ['Jack','Queen','King']:
            value += 10
        elif rank == 'Ace':
            value += 11
            aces += 1
        else:
            value += int(rank)

    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value

print("\nYour hand:", format_hand(player_hand))
print("Dealer shows:", f"{dealer_hand[0][0]} of {dealer_hand[0][1]}")
print("\nCard Value:",cal_hand_val(player_hand))