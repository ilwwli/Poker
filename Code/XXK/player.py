<<<<<<< HEAD:Code/XXK/player.py
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
=======
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
    
def removeCards():
    print '****** Code here *****'

def strategy():
    print '****** Code here *****'

def boardCards():
    print '****** Code here *****'
>>>>>>> 262024cae9f6d27ac562d5064df954e664222f62:documents/player.py
