import card
import board
from card import buildPoker
from card import shuffle
class Player:
    def __init__(self, name, boardpointer):
        self.name = name
        self.cards = []
        self.board = boardpointer

    def initial_cards(self, cardlist):
        self.cards = cardlist

    def display_cards(self):
        self.cards.sort()
        for card in self.cards:
            print(card)
    
    def play_cards(self, cardlist):
        for card in cardlist:
            self.cards.remove(card)

    def turn(self, last_player_claim = {}):        
        print("Last Player Claims He played %d of %s\n" % last_claim_length, last_claim_rank)
        print("There are %d cards on the deck at present\n" % len(display))
        print("Your hand is:\n")
        self.display_cards()

        choices = {'Pass' : self.Pass(argu)}
        if not last_player_claim:


        display = self.board.GetDisplayArea()
        actual_played = display[-last_claim_length :]

        print("Your Options are as follows:\n")
        choice = 0
        while choice != 1 and choice != 2 and choice != 3:
            choice = input("Follow : 1\t Doubt : 2\t Pass : 3\n")
        if choice == 1:


        elif choice == 2:

        else:

        




