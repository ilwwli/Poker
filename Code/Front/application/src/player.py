#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter
from threading import Event
from . import card
class Player:
    def __init__(self, name):
        # attributes        
        self.name = name
        self.cards = []
        # C/S arguments
        self.args = {}
        self.new_turn = False
        # C/S syn control
        self.turn_result_available = Event()  # server can get result        
        self.turn_start = Event()  # client should gather input        

    # def __eq__(self, other):
    #     return self.name == other.name

    # def __hash__(self):
    #     return hash('hash_of' + self.name)

    def initial_cards(self, cardlist):
        self.cards = cardlist

    # ---- interface for server ----
    def play_cards(self, cardlist):
        for card in cardlist:
            self.cards.remove(card)

    def insert_cards(self, cardlist):
        self.cards += cardlist

    def get_turn(self, new_turn) -> dict:
        self.new_turn = new_turn
        self.turn_start.set()
        self.turn_result_available.wait()
        self.turn_result_available.clear()
        return self.args
    # -------- END --------

    # ---- interface for client ----
    def refresh(self) -> list:
        if self.turn_start.is_set():
            if self.new_turn:
                options = ['Claim']
            else:
                options = ['Follow', 'Question', 'Pass']
            return [self.cards,options]
        else:
            return [self.cards,[]]

    def send_choices(self, option:str, *cardlist:list, claim:dict = {}) -> bool:
        if self.turn_start.is_set():
            self.turn_start.clear()
            self.args['Choice'] = option # option should be 'Claim', 'Question', 'Pass', 'Follow'
            if cardlist:
                self.args['Cards'] = cardlist
            if claim and option == 'Claim':
                self.args['Claim'] = claim
            return True
        else:
            return False
    # -------- END --------
