# -*- coding: utf-8 -*
class card:
    def __init__(self, suit, rank):
        self.suit = suit  # suit is poker suit
        self.rank = rank  # rank is poker number

def buildPoker():
    cards = []
    NumberCards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    ColorCards = ['J', 'Q', 'K', 'A']
    suits = ['H', 'S', 'D', 'C'] # H for Hearts, S for Spades, D for Diamonds, C for Clubs.
    for suit in suits:
        for NumberCard in NumberCards:
            cards.append(card(suit, NumberCard))
        for ColorCard in ColorCards:
            cards.append(card(suit, ColorCard))
    cards.append(card('N', 'w'))  # build the Jokers, N for None
    cards.append(card('N', 'W'))
    return cards

