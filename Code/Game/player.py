import card
import board
from functools import partial
from collections import Counter
class Player:
    def __init__(self, name, boardpointer):
        self.name = name
        self.cards = []
        self.board = boardpointer

    def initial_cards(self, cardlist):
        self.cards = cardlist

    def _display_cards(self):
        self.cards.sort()
        for card in self.cards:
            print(card)
    
    def play_cards(self, cardlist):
        for card in cardlist:
            self.cards.remove(card)
    
    def insert_cards(self, cardlist):
        self.cards += cardlist

    def turn(self, last_player_claim = {}): 
        # Must_Done_Process
        print("Your hand is:")
        self._display_cards()               
        if last_player_claim:
            display = self.board.GetDisplayArea()
            #actual_playedactual_played = display[-last_player_claim[claim_length] :]
            # ******** #
            print("Last Player Claims He played %d '%s' cards" % last_claim_length, last_claim_rank)
            print("There are %d cards on the deck at present" % len(display))
        argu = {} # return arguments 

        # Generate Options
        options = {}
        if not last_player_claim:
            options['Claim'] = self._choose_claim
        else:
            options['Follow'] = partial(self._choose_follow, last_claim = last_player_claim)
            # options['Doubt'] = partial( self._choose_doubt, 
            #                             last_claim = last_player_claim,
            #                             actual_played_cards = actual_played)
            options['Doubt'] = self._choose_doubt
            options['Pass'] = partial(self._choose_pass, last_claim = last_player_claim)

        print("Your Options are as follows:")
        optionlist = []
        for ind, op in enumerate(options, 1):
            print("%s : %d" % (op, ind),  end = '\t')
            optionlist.append(op)
        choice = 0
        while choice <= 0 or choice >= len(optionlist):
            choice = input("Input your choice:")
        option[optionlist[choice - 1]](argu)

        # Final Judgements
        if not self.cards:
            argu['winned'] = True
        else:
            argu['winned'] = False
        return argu

    def _choose_doubt(self, argu:dict):
        argu['Doubt'] = True
    
    def _choose_follow(self, argu:dict, last_claim):
        num = float('inf')
        Print("Last player claims rank %s" % last_claim['claim_rank'])
        while num > len(self.cards):
            num = input("Type how many cards you want to follow:")
        cardlist = self._input_card_list(num)
        ## ARGU CHANGEv*****
        #self._play_cards(cardlist)
        #self.board.Display(cardlist)

    def _choose_pass(self, argu:dict, last_claim):
        #argu['Claim'] = last_claim
        argu['Pass'] = None        

    def _choose_claim(self, argu:dict):
        print("It's your arbitary turn now, just claim what you want:")
        print("Claim example: 5 J for 5 'J' cards")
        claim = []
        while 1:
            claim = Input("Please make your claim:")
            if len(claim) != 2:
                continue
            if not claim[0].isdigit:
                continue
            if len(claim[1]) != 1 or claim[1] not in \
                ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                continue            
            break
        argu['Claim'] = {'claim_length' : int(claim[0]), 'claim_rank' : claim[1]}
        cardlist = self._input_card_list(int(claim[0]))
        ## ARG CHANGE
        #self._play_cards(cardlist)
        #self.board.Display(cardlist)

    def _input_card_list(self, num) -> cardlist:
        print("""   Please Input Card List, Example: 
                    H5/h5 for five of hearts, 
                    ww/Ww for joker, WW/wW for JOKER
                    sj/sJ/Sj/SJ for jack of spades""")
        while 1:
            string = Input("Input now:")
            templist = string.strip().split()
            cardlist = [Card(suit, rank) for cardstr in templist 
                        for suit, rank in cardstr.upper()]
            if len(cardlist) != num:
                continue
            if  all(map(card.Card.islegal, cardlist)):
                if all(map( lambda x: x>0, 
                            (Counter(self.cards) - Counter(cardlist)).values()))
                return cardlist

    def print_log(self, string):
        print(string)
           





        




