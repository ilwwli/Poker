#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Card():
    def __init__(self, suit, rank):
        self.suit = suit  # suit is poker suit
        self.rank = rank  # rank is poker number
    def __str__(self):
        d = {'H':u'♥', 'S':u'♠', 'D':u'♦', 'C':u'♣', 'N':None}
        if d[self.suit]:
            return d[self.suit] + str(self.rank)
        else:
            return u'joker' if self.rank == 'w' else u'JOKER'

    
class FullDeck():
    cards = []
    def __init__(self):
        if FullDeck.cards:
            return
        NumberCards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        ColorCards = ['J', 'Q', 'K', 'A']
        suits = ['H', 'S', 'D', 'C'] # H for Hearts, S for Spades, D for Diamonds, C for Clubs.
        for suit in suits:
            for NumberCard in NumberCards:
                FullDeck.cards.append(Card(suit, NumberCard))
            for ColorCard in ColorCards:
                FullDeck.cards.append(Card(suit, ColorCard))
        FullDeck.cards.append(Card('N', 'w'))  # build the Jokers, N for None
        FullDeck.cards.append(Card('N', 'W'))

    @classmethod
    def GetFullDeck(self):
        return FullDeck.cards.copy()

if __name__ == "__main__":
    FullDeck()
    for i in FullDeck.GetFullDeck():
        print(i, end = '\t')
    print()