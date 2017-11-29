import card
from card import buildPoker
from card import shuffle
class player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def InitialCards(self, cards):
        self.cards = cards

    def displayCards(self):
        for card in self.cards:
            print(card)

    def sortedCards(self):
        return self.cards.sort()
    
    def removeCards():
        print '****** Code here *****'

def strategy():
    print '****** Code here *****'

def boardCards():
    print '****** Code here *****'
