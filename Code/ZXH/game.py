#!/usr/bin/env python
# -*- coding: utf-8 -*-
import card
from random import shuffle

class gameboard():
    def __init__(self):
        self.Deck = []
        self.DiscardPile = []
        self.DisplayArea = []
        return self
    
    def Reinitialize(self, NumOfDecks = 2):
        self.Deck = [card.FullDeck.GetFullDeck() for i in NumOfDecks]
        self.DiscardPile.clear()
        self.DisplayArea.clear()
        shuffle(self.Deck)
        return self
    
    def InitializeHands(self, CardsForEachPlayer, NumOfPlayers = 4):
        if len(self.Deck) < CardsForEachPlayer * NumOfPlayers:
            return 0
        temp = []
        for i in range(NumOfPlayers):
            temp += self.Deck[i * CardsForEachPlayer : (i + 1) * CardsForEachPlayer]
        self.Deck[0 : CardsForEachPlayer * NumOfPlayers] = []
        return temp

    def Draw(self):
        return self.Deck.pop() if self.Deck else 0

    # def DrawMultiple(self, num):
    #     index = len(self.Deck)
    #     if index < num:
    #         return 0
    #     temp = self.Deck[index - num: index]
    #     self.Deck[index - num:index] = []
    #     return temp

    def ShowDisplayArea(self):
        return self.DisplayArea

    def RefreshDisplayArea(self, cardlist):
        self.DiscardPile += self.DisplayArea
        self.DisplayArea = cardlist
    
    def Discard(self, cardlist):
        self.DiscardPile += cardlist

    def ShuffleDeck(self):
        return shuffle(self.Deck) 
    
if __name__ == "__main" :
    gb = gameboard().Reinitialize()

