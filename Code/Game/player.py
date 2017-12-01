#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter
import card
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

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

    def turn(self, new_turn):
        # Must_Done_Process
        print("Your hand is:")
        self._display_cards()
        arg = {} # return arguments

        # Generate Options
        options = {}
        if new_turn:
            options['Claim'] = self._choose_claim
        else:
            options['Follow'] = self._choose_follow
            options['Doubt'] = self._choose_doubt
            options['Pass'] = self._choose_pass

        print("Your Options are as follows:")
        optionlist = []
        for ind, option in enumerate(options, 1):
            print("%s : %d" % (option, ind), end='\t')
            optionlist.append(option)
        choice = 0
        while choice <= 0 or choice >= len(optionlist):
            choice = input("Input your choice:")
        arg['Choice'] = optionlist[choice - 1]
        options[optionlist[choice - 1]](arg) # Execute Option Function

        # Final Judgements
        arg['Win'] = not bool(self.cards)
        return arg

    def _choose_doubt(self, arg: dict):
        arg['Doubt'] = True
        return

    def _choose_follow(self, arg: dict):
        num = float('inf')
        while num > len(self.cards):
            num = input("Type how many cards you want to follow:")
        arg['Cards'] = self._input_card_list(num)
        return

    def _choose_pass(self, arg: dict):
        return

    def _choose_claim(self, arg: dict):
        print("A new round start with you, please claim.")
        print("Claim example: 5 J for 5 'J' cards, you cannot claim 'W' or >10 cards")
        claim = []
        while 1:
            claim = input("Please make your claim:")
            if len(claim) != 2:
                continue
            # judge Number argument
            if not claim[0].isdigit:
                continue
            else:
                claim[0] = int(claim[0])
                if claim[0] <= 0 or claim[0] > 10:
                    continue
            # judge Rank argument
            if len(claim[1]) != 1 or claim[1] not in \
                ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                continue
            break
        arg['Claim'] = {'claim_length' : int(claim[0]), 'claim_rank' : claim[1]}
        arg['Cards'] = self._input_card_list(int(claim[0]))

    def _input_card_list(self, num) -> list:
        print("""   Please Input Card List, Example:
                    H5/h5 for five of hearts,
                    ww/Ww for joker, WW/wW for JOKER
                    sj/sJ/Sj/SJ for jack of spades""")
        while 1:
            string = input("Input now:")
            templist = string.strip().split()
            cardlist = [card.Card(suit, rank) for cardstr in templist
                        for suit, rank in cardstr.upper()]
            if len(cardlist) != num:
                continue
            if  all(map(card.Card.islegal, cardlist)):
                if all(map(lambda x: x > 0, (Counter(self.cards) - Counter(cardlist)).values())):
                    return cardlist

    def print_log(self, string):
        print(string)
