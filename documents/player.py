import card
from card import buildPoker
from card import shuffle
class player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

def displayCards(player):
    print 'Cards for' + player.name + 'are: '
    for card in player.cards:
        print card.suit, card.rank

def sortedCards(player):
    # ### code here ####
    print 'Code here'